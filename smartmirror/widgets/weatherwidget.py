# -*- coding: utf-8 -*-
from dataclasses import dataclass
from enum import IntEnum
import pyowm
from smartmirror.widgets.basewidget import TextWidget


class Alignment(IntEnum):
    LEFT = 0
    RIGHT = 1

@dataclass
class WeatherWidget(TextWidget):
    _owm_api_key: str = ''
    _celsius: bool = True

    def refresh_data(self):
        owm = pyowm.OWM(self._owm_api_key)
        try:
            observation = owm.weather_at_place('Linkoping,SE')
            w = observation.get_weather()
            print(w)

            temp = str(w.get_temperature('celsius').get('temp')) + ' °C' if self._celsius else str(w.get_temperature('fahrenheit').get('temp')) + ' °F'
            return temp
        except ValueError as e:
            print(e)
            return 0
        except pyowm.exceptions.api_response_error.UnauthorizedError as e:
            return str(e)

