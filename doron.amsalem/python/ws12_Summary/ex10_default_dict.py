# basheer
class DEFUALT_DICT(dict):
    def __init__(self, num):
        """default dictionary is dict that return default value for not existing key"""
        self.default_key = num
        super().__init__()

    def __getitem__(self, key):
        """return value for existing key or default value if not"""
        try:
            return self.__dict__[key]
        except KeyError:
            return self.default_key

    def __setitem__(self, key, value):
        self.__dict__[key] = value



if __name__ == "__main__":
    a = DEFUALT_DICT(0)
    a[5] = "g"
    print(a[4])
    print(a[5])
    print(a.__dict__)





