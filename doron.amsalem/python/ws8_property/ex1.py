from numbers import Number
class Point(object):
    """class of point with two attributes: x, y"""
    def __init__(self, a = 0.0, b = 0.0):
        """create new object of point in conditions of passing number as elements"""
        if isinstance(a, Number) and isinstance(b, Number):
            self.__x = a
            self.__y = b

        else:
            raise TypeError("coordination must be numbers ")

    def get_x(self):
        """return value of x"""
        return self.__x

    def set_x(self, a):
        """set new value to x attribute"""
        if isinstance(a, Number):
            self.__x = a
        else:
            raise TypeError("coordination must be numbers ")

    def get_y(self):
        """return value of y"""
        return self.__y

    def set_y(self, a):
        """set new value to y attribute"""
        self.__y = a

    x_modi = property(get_x, set_x, doc="x coordinate property")
    y_modi = property(get_y, set_y, doc="y coordinate property")



if __name__ == "__main__":
    p = Point()
    print(p.x_modi)
    print(p.__dict__)
    p.x_modi = "sfs"
    print(p.x_modi)

