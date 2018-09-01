from unittest import TestCase
import smartmirror.pointshape


class TestPointShapeCircle(TestCase):
    def test_amount_of_points(self):
        circle = smartmirror.pointshape.Circle(10, 0, 0, _points=10)
        amount_of_points_generated = len(circle.calculate_points())
        print(amount_of_points_generated)
        # TODO this one fails
        assert amount_of_points_generated == 10

    def test_point_distance(self):
        pass
        # circle = smartmirror.pointshape.Circle(10, 0, 0, _point_distance=10)
        # points = circle.calculate_points()
        # for p