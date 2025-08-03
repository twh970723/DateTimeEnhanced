import datetime
import os
from typing import List, Literal


class DateTimeEnhanced:
    def __init__(self):
        self.date: str = ""
        self.time: str = ""
        self.day: str = ""

    def today(self, include_info: list[Literal["date", "time", "day"]]):
        today_datetime = datetime.datetime.today()
        for item in include_info:
            item_lower = item.lower()
            if item_lower == "date":
                self.date = today_datetime.strftime("%Y-%m-%d")
            elif item_lower == "time":
                self.time = today_datetime.strftime("%H:%M:%S.%f")
            elif item_lower == "day":
                self.day = today_datetime.strftime("%A")

    def get_output(self, info_sequence: list[Literal["date", "time", "day"]], info_separator: str):
        info_data = {"date": self.date, "time": self.time, "day": self.day}
        info_data = {key: info_data[key] for key in info_sequence if key in info_data}
        return info_separator.join(info_data.values())
