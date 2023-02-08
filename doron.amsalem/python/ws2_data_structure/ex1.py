# interview by basheer
def only_str(ls):
    """ gets list and remove all element expt strings """
    i = 0
    while i < len(ls):
        if type(ls[i]) != str:
            del ls[i]
        else:
            i += 1


if __name__ == "__main__":
    ls = [3, 5, "doron", 5, "doron", "amsalem", 4, "infinity", 0]
    only_str(ls)
    print(ls)
