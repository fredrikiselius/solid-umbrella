from dataclasses import field
from typing import List, Tuple
from smartmirror import pointshape


class Entity:
    _color: Tuple[int, int, int, int]
    _shape: pointshape.Shape
    _shape_points: List[Tuple[int, int]]
    _shape_points_at_switch: List[Tuple[int, int]] = field(init=False)

    def transform(self, new_shape: pointshape.Shape):
        self._shape_points_at_switch = self.points

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, new: Tuple[int, int, int, int]):
        self._color = new

    @property
    def points(self) -> List[Tuple[int, int]]:
        return self._shape_points






