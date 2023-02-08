# interview by basheer
def unique_value(dictionery):
    """get dictionary and return list of unique values"""
    print(list(set(dictionery.values())))


if __name__ == "__main__":
    d = {"a": 3, "b": 4, "c": 4, "d": 5}
    unique_value(d)
