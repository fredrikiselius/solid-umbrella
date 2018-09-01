from dataclasses import dataclass, field
from datetime import datetime
from enum import IntEnum
from smartmirror.widgets.basewidget import TextWidget


class Alignment(IntEnum):
    LEFT = 0
    RIGHT = 1

@dataclass
class TimeWidget(TextWidget):
    DEFAULT_TIME_FORMAT: str = field(init=False, default='%H:%M')
    DEFAULT_DATE_FORMAT: str = field(init=False, default='%A %d %B')
    _time_format: str = DEFAULT_TIME_FORMAT
    _date_format: str = DEFAULT_DATE_FORMAT

    def refresh_data(self):
        now = datetime.today()
        time_str = now.strftime(self._time_format)
        date_str = now.strftime(self._date_format)
        return f'{time_str}\n{date_str}'