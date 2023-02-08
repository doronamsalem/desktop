from numbers import Number    # checking if var is number
from math import sqrt         # to get squarer root
class Point(object):
    """class of point with tow attributes: x, y
    """
    point_id = 0
    def __init__(self, a = 0.0, b = 0.0):
        """create point instance"""
        if isinstance(a, Number) and isinstance(b, Number):
            self.x = a
            self.y = b
            Point.point_id += 1
        else:
            print("the values aren`t numbers")
# ex 3
    def distance_from_origin(self):
        """return the distance from origin"""
        return sqrt(self.x * self.x + self.y * self.y)


p1 = Point(2, 2)

print(p1.point_id)

print(p1.distance_from_origin())

print(p1)

