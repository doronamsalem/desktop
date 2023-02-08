"""interview by basheer"""
def is_global(var):
    """
    :param var:
    :return if the var is global:
    """
    return var in globals()


def make_enclose_var():
    c = 6
    print(is_global("c"))


b = 4
if __name__ == "__main__":
    a = 3
    print(is_global("a"))
    print(globals())
    make_enclose_var()