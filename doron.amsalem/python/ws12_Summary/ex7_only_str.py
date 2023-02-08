# review by vica
def only_str(ls):
    """get a list\nremove all non str elements"""
    if type(ls) != list:
        raise TypeError

    x = 0
    while x < len(ls):
        if type(ls[x]) != str:
            del ls[x]
        else:
            x += 1


if __name__ == "__main__":
    s = ['1', 2, 3, "doron", "amsalem", 5, "infinity"]
    only_str(s)
    print(s)