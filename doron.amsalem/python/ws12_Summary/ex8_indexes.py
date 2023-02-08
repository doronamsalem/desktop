# review by vica
def list_indexes(ls):
    """get list\nprint index and there value"""
    assert type(ls) is list
    for ind, ele in enumerate(ls):
        print(ind, " ", ele)


def dict_keys(dictionary):
    """get dictionary\nprint index and there value"""
    assert type(dictionary) is dict
    for item in dictionary.items():
        print(item)


if __name__ == "__main__":
    ls = ['1', 2, 3, "doron", "amsalem", 5, "infinity"]
    dic = {1: "a", 2: "b", 3: "c"}

    list_indexes(dic)
    print(" ")
    dict_keys(dic)

