class X(object):
    def __init__(self):
        """create object X"""
        self.__a = 1

    def get_a(self):
        """return a attribute"""
        print("hello from get_a")
        return self.__a

    def set_a(self, a):
        """return a attribute"""
        self.__a = a

    a = property(get_a, set_a)


if __name__ == "__main__":
    y = X()
    print(y.a)
    y.a = 5
    print(y.a)
