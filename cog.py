from discord.ext import commands


class Timeouts(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.services = getattr(bot, 'r4_services', None)
        if self.services is None:
            raise RuntimeError('R4Bot runtime services are not available on bot.r4_services')

    @commands.Cog.listener()
    async def on_member_update(self, before, after):
        if not after.timed_out:
            return

        author_id = str(after.id)
        guild_id = str(after.guild.id)
        timeout_record = self.services.firebase.get_from_record(guild_id, 'Users', author_id)
        if timeout_record is None:
            timeout_record = {'timeouts': 1}
        else:
            timeout_record['timeouts'] = timeout_record.get('timeouts', 0) + 1

        self.services.firebase.update_record(guild_id, 'Users', author_id, timeout_record)


def setup(bot):
    bot.add_cog(Timeouts(bot))
