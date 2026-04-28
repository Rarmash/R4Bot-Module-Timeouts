from r4bot_sdk import register_hook_provider, unregister_hook_provider
MODULE_ID = "timeouts"
LEADERBOARD_PROVIDERS_HOOK = "leaderboards.providers"


class TimeoutsService:
    def __init__(self, module):
        self.module = module

    def register_hooks(self):
        register_hook_provider(
            self.module.bot,
            LEADERBOARD_PROVIDERS_HOOK,
            MODULE_ID,
            {
                "name": "timeouts",
                "description": "Посмотреть таблицу лидеров по тайм-аутам",
                "callback": self.module.show_timeouts_leaderboard,
            },
        )

    def unregister_hooks(self):
        unregister_hook_provider(self.module.bot, LEADERBOARD_PROVIDERS_HOOK, MODULE_ID)
