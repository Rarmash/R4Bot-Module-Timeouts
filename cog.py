import discord
from discord.ext import commands

from .service import TimeoutsService


def generate_timeout_leaderboard_lines(data_list):
    def get_place_icon(index):
        if index == 0:
            return "🥇"
        if index == 1:
            return "🥈"
        if index == 2:
            return "🥉"
        return f"{index + 1}."

    return "\n".join(
        f"{get_place_icon(index)} <@{user[0]}>: {user[1]}" for index, user in enumerate(data_list[:10])
    )


class Timeouts(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.services = getattr(bot, "r4_services", None)
        if self.services is None:
            raise RuntimeError("R4Bot runtime services are not available on bot.r4_services")
        self.service = TimeoutsService(self)
        self.service.register_hooks()

    def cog_unload(self):
        self.service.unregister_hooks()

    async def show_timeouts_leaderboard(self, ctx, server_data):
        users = self.services.firebase.get_all_records(str(ctx.guild.id), "Users") or {}
        leaderboard = [
            [user_id, user_data.get("timeouts", 0)]
            for user_id, user_data in users.items()
            if user_data.get("timeouts", 0) != 0
        ]
        leaderboard.sort(key=lambda items: items[1], reverse=True)

        total_timeouts = sum(user[1] for user in leaderboard)
        embed = discord.Embed(
            title="Лидеры по тайм-аутам",
            description=generate_timeout_leaderboard_lines(leaderboard),
            color=int(server_data.get("accent_color"), 16),
        )
        embed.set_footer(text=f"Всего получено {total_timeouts} тайм-аутов")
        await ctx.respond(embed=embed)

    @commands.Cog.listener()
    async def on_member_update(self, before, after):
        if not after.timed_out:
            return

        author_id = str(after.id)
        guild_id = str(after.guild.id)
        timeout_record = self.services.firebase.get_from_record(guild_id, "Users", author_id)
        if timeout_record is None:
            timeout_record = {"timeouts": 1}
        else:
            timeout_record["timeouts"] = timeout_record.get("timeouts", 0) + 1

        self.services.firebase.update_record(guild_id, "Users", author_id, timeout_record)


def setup(bot):
    bot.add_cog(Timeouts(bot))
