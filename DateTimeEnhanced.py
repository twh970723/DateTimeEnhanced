import datetime
from typing import Literal


class DateTimeEnhanced:
    def __init__(self):
        self.date: str = ""
        self.time: str = ""
        self.day: str = ""
        self.week_day: str = ""
        self.default: str = ""

    def set_value(self, date_time: datetime.datetime, first_day_of_week: Literal["sunday", "monday", "iso"]):
        self.date = date_time.strftime("%Y-%m-%d")
        self.time = date_time.strftime("%H:%M:%S.%f")
        self.day = date_time.strftime("%A")
        self.week_day = {
            "sunday": f"{int(date_time.strftime('%U')) + 1}.{(date_time.weekday() + 1) % 7}",
            "monday": f"{int(date_time.strftime('%W')) + 1}.{date_time.weekday()}",
            "iso": f"{date_time.isocalendar().week}.{date_time.isocalendar().weekday}"
        }.get(first_day_of_week)
        self.default = str(date_time)

    def today(self, first_day_of_week: Literal["sunday", "monday", "iso"]):
        self.set_value(datetime.datetime.today(), first_day_of_week)

    def last_n_day(self, last_n_day: int, first_day_of_week: Literal["sunday", "monday", "iso"]):
        self.set_value(datetime.datetime.today() - datetime.timedelta(days=last_n_day), first_day_of_week)

    def last_n_week(self, last_n_week: int, first_day_of_week: Literal["sunday", "monday", "iso"]):
        self.set_value(datetime.datetime.today() - datetime.timedelta(weeks=last_n_week), first_day_of_week)

    def get_output(self, info_sequence: list[Literal["default", "date", "time", "day", "week_day"]], info_separator: str):
        info_data = {"default": self.default, "date": self.date, "time": self.time, "day": self.day, "week_day": self.week_day}
        info_data = {key: info_data[key] for key in info_sequence if key in info_data}
        return info_separator.join(info_data.values())
