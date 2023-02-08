#review by vica
def increment_list(ls):
    """get a list of number\nincrement each of them"""
    for x in range(len(ls)):
        ls.insert(x, ls.pop(x) + 1)


if __name__ == "__main__":
    s = [1, 2, 3, 4, 5]
    increment_list(s)
    print(s)