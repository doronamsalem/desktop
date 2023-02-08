class Property:
    def __init__(self, fget=None, fset=None, fdel=None, doc=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel
        self.doc = doc

    def Getter(self):
        return self._x

    def Setter(self, value): self._x = value

    def Deleter(self): del self._x

    x = property(Getter, Setter, Deleter, "I'm the 'x' property.")


class X:
    def __init__(self, val):
        self.__x = int(val)

    @Property
    def x(self):
        return self.__x

    @x.Setter
    def x(self, val):
        self.__x = val

    @x.Deleter
    def x(self):
        del self.__x


x = X(4)
print(x.__dict__)
print(X(0).x)




x = Property()
print(dir(x))
print(dir(Property))
print(x.__dict__)
print(Property.__dict__)


class GFG(object):
    __slots__ = ['a', 'b', '__dict__']
    c = 8
    def __init__(self, *args, **kwargs):
        self.a = 1
        self.b = 2
        self.g = 5


if __name__ == "__main__":
    instance = GFG()
    print(GFG.c)
    print(instance.__slots__)
    print(instance.__dict__)


