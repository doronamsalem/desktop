class X(object):
    """Example class"""
    def __init__(self):
        """init function for class X"""
        self.a = 1
        self._a = 2
        self.__a = 3

    def get_hidden_attribute(self):
        """return the hidden attributes"""
        return self._a, self.__a

    def set_hidden_attribute(self, a, b):
        """return the hidden attributes"""
        self._a = a
        self.__a = b


if __name__ == "__main__":
    x = X()
    print(x.a)
    print(x._a)
    # print(x.__a)
    print(x.__dict__)
    x.set_hidden_attribute(2, 5)
    print(x._X__a)
    print(x.get_hidden_attribute())