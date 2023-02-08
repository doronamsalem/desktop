from numbers import Number
class Point(object):
    """class of point with two attributes: x, y"""
    point_id = 0
    def __init__(self, a = 0.0, b = 0.0):
        """create new object of point in conditions of passing number as elements"""
        if isinstance(a, Number) and isinstance(b, Number):
            self.x = a
            self.y = b
            Point.point_id += 1
        else:
            print("the values aren`t numbers")

# exercise 1
    def __str__(self):
        """ :return: string with explanation about object"""
        return "Point({}, {})".format(float(self.x), float(self.y))

# exercise 2
    def __add__(self, other):
        "add to two coordinates of two points to new point coordinate "
        return f"Point({float(self.x + other.y)}, {float(self.x + other.y)})"

    def __sub__(self, other):
        """subtract one point coordinates from second"""
        return f"Point({float(self.x - other.x)}, {float(self.y - other.y)})"

    def __mul__(self, other):
        """multiple of coordinates by scalar"""
        self.x *= other
        self.y *= other
        return self

    def __truediv__(self, other):
        """division of coordinates by scalar"""
        self.x /= other
        self.y /= other
        return self

# exercise 3
    def __del__(self):
        """subtract number of object after delete one"""
        Point.point_id -= 1

    @classmethod
    def get_counter(cls):
        """return number of objects from point class"""
        return cls.point_id

# exercise 4
    def __len__(self):
        """return number of attributes in object class"""
        print(len(self.__dict__))

if __name__ =="__main__":
    p = Point(1, 3)
    p.__truediv__(0)
