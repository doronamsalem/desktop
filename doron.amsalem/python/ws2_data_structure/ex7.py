# interview by sara
def dict_to_list(dictionary):
    """
    :param dictionary:
    :return list of tuples:
    """
    lis = []
    while len(dictionary) > 0:
        lis.insert(0, dictionary.popitem())
    return lis


if __name__ == "__main__":
    d = {"a": 1, "b": 2, "c": 3}
    ls = dict_to_list(d)
    print(ls)
