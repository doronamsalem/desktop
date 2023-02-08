# review by vica
def str_dunder():
    """print all str dunder methods with for"""
    only_dunder = []
    for x in dir(str):
        if not x.startswith("__", 0, 2) and not x.startswith("__", -2, len(x)):
            only_dunder.append(x)
    return only_dunder

def str_dunder_comp():
    """print all str dunder methods with comprehension"""
    only_dunder = [x for x in dir(str) if not x.startswith("__", 0, 2) and not x.startswith("__", -2, len(x))]
    return only_dunder

def str_dunder_filter():
    """print all str dunder methods with filter"""
    only_dunder = filter(lambda x: not x.startswith("__", 0, 2) and not x.startswith("__", -2, len(x)), dir(str) )
    return list(only_dunder)

if __name__ == "__main__":
    str_dunder()
    str_dunder_comp()
    str_dunder_filter()
