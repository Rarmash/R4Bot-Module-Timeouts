LEADERBOARD_PROVIDERS_HOOK = "leaderboards.providers"


class TimeoutsService:
    def __init__(self, module):
        self.module = module

    def register_hooks(self):
        self.module.register_hook_provider(
            LEADERBOARD_PROVIDERS_HOOK,
            {
                "name": "timeouts",
                "description": "Посмотреть таблицу лидеров по тайм-аутам",
                "callback": self.module.show_timeouts_leaderboard,
            },
        )

    def unregister_hooks(self):
        self.module.unregister_hook_provider(LEADERBOARD_PROVIDERS_HOOK)
