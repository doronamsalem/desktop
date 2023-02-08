# code review by naan
class X:
    __created = False
    """class of x"""
    #__slots__ = ['a']
    def __init__(self, a):
        self.a = a
        print(self.__dict__)
        self.__class__.__created = True

    def __getattr__(self, item):
        """print message if user asked for a non existing attribute"""
        return "there isn`t attribute {}".format(item)

    def __setattr__(self, key, value):
        """forbidden set attributes except builtins"""
        if self.__class__.__created == False or key in self.__dict__:
            self.__dict__[key] = value
        else:
            raise "you cant add new attribute"


y = X(1)
print(y.__dict__)
print(y.a)
y.a = 3
y.b = 5
print(y.b)

