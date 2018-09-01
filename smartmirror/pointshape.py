from __future__ import division
import math
from dataclasses import dataclass, field
from typing import Union, List, Tuple
from enum import IntEnum
import itertools


def line(p1, p2):
    A = (p1[1] - p2[1])
    B = (p2[0] - p1[0])
    C = (p1[0]*p2[1] - p2[0]*p1[1])
    return A, B, -C

def intersection(L1, L2):
    D  = L1[0] * L2[1] - L1[1] * L2[0]
    Dx = L1[2] * L2[1] - L1[1] * L2[2]
    Dy = L1[0] * L2[2] - L1[2] * L2[0]
    if D != 0:
        x = Dx / D
        y = Dy / D
        return x,y
    else:
        return False

class Shape(IntEnum):
    CIRCLE = 1

@dataclass
class Circle:
    _radius: float

    _center_x: Union[int, float]
    _center_y: Union[int, float]

    # Either _points or _point_distance must be set
    _points: int = field(default=None) # Amount of points that will make the circle
    _point_distance: Union[int, float] = field(default=None) # Distance between points
    _use_points: bool = field(init=False, default=False)  # Used to determine calculation mode

    def __post_init__(self):
        if self._points is None and self._point_distance is None:
            raise ValueError('Either _points or _point_distance must be set')

        self._use_points = self._points is not None

        # Check the ratio between radius and point distance is ok
        if not self._use_points and not self._point_distance <= (2 * self._radius):
            raise ValueError('point distance must be smaller then the circle diameter')

    def calculate_points(self, start_angle: float = 0)-> List[Tuple[float, float]]:
        angle = start_angle

        # Set how much to increase the angle for each iteration based on the calculation mode

        if self._use_points:
            angle_step: float = (2*math.pi) / self._points
            points_to_generate = self._points
        else:
            angle_step = 2 * math.asin(self._point_distance / (2 * self._radius))
            points_to_generate = (2 * math.pi) / angle_step

        point_counter = 0
        points: List[Tuple[float, float]] = []
        while point_counter < points_to_generate:
            points.append((self._center_x + self._radius * math.cos(angle), self._center_y + self._radius * math.sin(angle)))
            angle += angle_step
            point_counter += 1
        return points

    @property
    def radius(self) -> float:
        return self.radius

    @radius.setter
    def radius(self, r: float):
        self._radius = r

    @property
    def num_points(self) -> int:
        return self._points

    @num_points.setter
    def num_points(self, n: int):
        self._points = n
        self._use_points = True

    @property
    def point_distance(self) -> float:
        return self._point_distance

    @point_distance.setter
    def point_distance(self, distance: float):
        self._point_distance = distance

@dataclass
class Rectangle:
    _width: Union[int, float]
    _height: Union[int, float]

    _center_x: Union[int, float]
    _center_y: Union[int, float]

    # Either _points or _point_distance must be set
    _points: int = field(default=None) # Amount of points that will make the circle
    _point_distance: Union[int, float] = field(default=None) # Distance between points
    _use_points: bool = field(init=False, default=False)  # Used to determine calculation mode

    def __post_init__(self):
        if self._points is None and self._point_distance is None:
            raise ValueError('Either _points or _point_distance must be set')

        self._use_points = self._points is not None

        # Check the ratio between radius and point distance is ok
        if not self._use_points and not self._point_distance <= (2 * self._radius):
            raise ValueError('point distance must be smaller then the circle diameter')

    def calculate_points(self) -> List[Tuple[Union[int, float]]]:
        # perimeter: Union[int, float] = 2*self._width + 2*self._height
        # vertical_points = int(self._points * ((2 * self._height) / perimeter)) //
        # horizontal_points = self._points - vertical_points
        # distance_between_points: Union[int, float] = perimeter / self._points
        #
        # print(f'vertical {vertical_points} horizontal {horizontal_points}')
        # points = []
        # for i in range(vertical_points // 2):
        #     points.append((self._center_x - (self._width / 2) + i * distance_between_points, self._center_y + self._height / 2))
        #     points.append((self._center_x - (self._width / 2) + i * distance_between_points, self._center_y - (self._height / 2)))
        #     points.append((self._center_x - (self._width / 2) + i * distance_between_points, self._center_y + self._height / 2))
        r = max(self._width, self._height) #math.hypot(self._width / 2, self._height / 2)
        angle = 0
        angle_step = (2 * math.pi) / self._points
        points = []
        sign = lambda x : 1 if x >= 0 else -1
        lines = [line([self._center_x - self._width / 2])]
        while angle <= (2 * math.pi):
            # if angle >= mathp.pi / 4 and angle <=
            # if math.pi / 4 <= angle <= (math.pi - math.pi / 4) or math.pi + (math.pi / 4) <= angle <= 2 * math.pi:
            #     r = math.
            c_x = r * math.cos(angle)
            c_y = r * math.sin(angle)
            print(c_x, c_y)
            assert abs(c_x) > self._width / 2 or abs(c_y) > self._height / 2
            x = sign(c_x) * (self._width / 2) if (self._width / 2) < abs(c_x) else c_x
            y = sign(c_y) * (self._height / 2) if (self._height / 2) < abs(c_y) else c_y
            x += self._center_x
            y += self._center_y
            # x = min(sign(c_x) * (self._width / 2), c_x)
            # y = min(sign(c_y) * (self._height / 2), c_y)
            points.append((x, y))
            angle += angle_step
        print(list(itertools.permutations([])))
        return points
