from pygame import Surface, font
from dataclasses import dataclass, field
from datetime import datetime
from typing import Tuple
from enum import IntEnum
from abc import ABCMeta, abstractmethod
import time

class Alignment(IntEnum):
    LEFT = 0
    RIGHT = 1

@dataclass
class TextWidget(Surface, metaclass=ABCMeta):
    _last_refresh: float = field(init=False, default=0)
    _size: Tuple[int, int] = field(default=(200, 50))
    _font: str = 'Helvetica'
    _font_size: int = 20
    _font_color: Tuple[int, int, int] = field(default=(255, 255, 255))
    _align: Alignment = Alignment.RIGHT
    _padding: Tuple[int, int] = field(default=(10, 10))
    _font_antialias: bool = False
    _refresh_interval: int = 30 # How often should the refresh_data function be called

    def __post_init__(self):
        Surface.__init__(self, self._size)
        self._font_obj = font.SysFont(self._font, self._font_size)

    @abstractmethod
    def refresh_data(self) -> str:
        """
        Should return the updated data in a string.
        Use of newline for multiple rows
        :return:
        """
        pass

    def update_widget(self):
        if time.time() - self._last_refresh < self._last_refresh: return
        # Update data to be displayed
        data: str = self.refresh_data()
        self._last_refresh = time.time()

        if not isinstance(data, str):
            data = 'Error'
            bg_color = (255, 0, 0)
        else:
            bg_color = (0, 255, 0)

        lines = data.split('\n')
        render_objects = [self._font_obj.render(line, self._font_antialias, self._font_color) for line in lines]
        required_width = max(self._font_obj.size(line)[0] for line in lines) + self._padding[0] * 2


        # Calculate anchor points for each line
        if self._align == Alignment.RIGHT:
            anchors = [(self.width - self._font_obj.size(line)[0] - self.h_padding, # x anchor
                        self.v_padding * (i + 1) + i * self._font_size)             # y anchor
                       for i, line in enumerate(lines)]
        else:
            anchors = [(self.h_padding, self.v_padding * (i + 1) + self._font_size) for i, line in enumerate(lines)]

        Surface.__init__(self, (required_width, anchors[-1][1] + self._font_size + self.v_padding))
        self.fill((255,0,0))
        self.blits(list(zip(render_objects, anchors)))

    @property
    def width(self) -> int:
        return self._size[0]

    @property
    def height(self) -> int:
        return self._size[1]

    @property
    def h_padding(self) -> int:
        return self._padding[0]

    @property
    def v_padding(self) -> int:
        return self._padding[1]