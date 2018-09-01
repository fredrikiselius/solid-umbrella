import math
from unittest import TestCase
import smartmirror.pointshape


class TestPointShapeCircle(TestCase):
    def test_amount_of_points(self):
        """
        Assert that the calculate_points function returns the right amount of points
        """
        points_to_generate = 10
        circle = smartmirror.pointshape.Circle(10, 0, 0, _points=points_to_generate)
        amount_of_points_generated = len(circle.calculate_points())
        # TODO this one fails
        print(f'Points to generate {points_to_generate}, points generated {amount_of_points_generated}')
        assert amount_of_points_generated == points_to_generate

    def test_point_distance(self):
        """
        Assert that the distance between each neighbor point pair
        is close enough (error < error_margin) to set_point_distance
        """
        set_point_distance = 10
        error_margin = 0.01
        circle = smartmirror.pointshape.Circle(10, 0, 0, _point_distance=set_point_distance)
        points = circle.calculate_points()
        distances = [math.hypot(points[i][0] - points[i-1][0], points[i][1] - points[i-1][1]) for i in range(1, len(points))]

        print(f'Point distance: {set_point_distance}')
        print(f'Allowed error margin: {error_margin}')
        print(f'Calculated distances:\n {distances}')
        assert False#all([abs(set_point_distance - d) < error_margin for d in distances])