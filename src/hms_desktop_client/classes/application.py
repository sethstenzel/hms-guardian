class Application:
    def __init__(
            self,
            application_name:str,
            application_daily:int,
            application_daily_max:int,
            application_weekly:int,
            application_weekly_max:int,
            application_time_blocks:int,
            application_message:str
        ):
        self.name = application_name
        self.daily = application_daily
        self.daily_max = application_daily_max
        self.weekly = application_weekly
        self.weekly_max = application_weekly_max
        self.time_blocks = application_time_blocks
        self.message = application_message