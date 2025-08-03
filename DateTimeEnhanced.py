import datetime
import os
from typing import List, Literal


class DateTimeEnhanced:
    def __init__(self):
        self.date: str = ""
        self.time: str = ""
        self.day: str = ""
        self.week: str = ""
        self.default: str = ""

    def set_value(self, date_time: datetime.datetime, first_day_of_week: Literal["sunday", "monday", "iso"]):
        self.date = date_time.strftime("%Y-%m-%d")
        self.time = date_time.strftime("%H:%M:%S.%f")
        self.day = date_time.strftime("%A")
        self.week = {
            "sunday": f"{int(date_time.strftime('%U')) + 1}.{(date_time.weekday() + 1) % 7}",
            "monday": f"{int(date_time.strftime('%W')) + 1}.{date_time.weekday()}",
            "iso": f"{date_time.isocalendar().week}.{date_time.isocalendar().weekday}"
        }.get(first_day_of_week)
        self.default = str(date_time)

    def today(self, first_day_of_week: Literal["sunday", "monday", "iso"]):
        current_day = datetime.datetime.today()
        self.set_value(current_day, first_day_of_week)

    def last_n_day(self, last_n_day: int, first_day_of_week: Literal["sunday", "monday", "iso"]):
        current_day = datetime.datetime.today() - datetime.timedelta(days=last_n_day)
        self.set_value(current_day, first_day_of_week)

    def last_n_week(self, last_n_week: int, first_day_of_week: Literal["sunday", "monday", "iso"]):
        current_day = datetime.datetime.today() - datetime.timedelta(weeks=last_n_week)
        self.set_value(current_day, first_day_of_week)

    def get_output(self, info_sequence: list[Literal["default", "date", "time", "day", "week"]], info_separator: str):
        info_data = {"default": self.default, "date": self.date, "time": self.time, "day": self.day, "week": self.week}
        info_data = {key: info_data[key] for key in info_sequence if key in info_data}
        return info_separator.join(info_data.values())
