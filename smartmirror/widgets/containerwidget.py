from pygame import Surface
from dataclasses import dataclass, field
from typing import List, Tuple

@dataclass
class WidgetContainer(Surface):
    _size: Tuple[int, int] = field(default=(100, 100))
    _padding: Tuple[int, int] = field(default=(10,10))

    _widgets: List[Surface] = field(default_factory=list)

    def __post_init__(self):
        Surface.__init__(self, (self._size))

    def add_widget(self, widget: Surface):
        self._widgets.append(widget)

    def draw_widgets(self):
        required_width = max([w.get_width() for w in self.widgets]) + self._padding[0] * 2
        print(f'Required size: {required_width}')
        if  required_width > self._size[0]:
            Surface.__init__(self, (required_width, self._size[1]))
        self.fill((0,255,0))
        offset_height: int = 0
        for i, widget in enumerate(self._widgets):
            self.blit(widget, (self._padding[0], (self._padding[1] * (i + 1)) + offset_height))
            _, h = widget.get_size()
            offset_height += h

    @property
    def widgets(self) -> List[Surface]:
        return self._widgets