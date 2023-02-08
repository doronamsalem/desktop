# interview by basheer
def identical_occurrence(lis1, lis2):
    """gets 2 lists and return list with the identical elements"""
    iden_list = []
    for element1 in lis1:
        if lis2.count(element1) > 0:
            iden_list.append(element1)
    return iden_list


if __name__ == "__main__":
    list1 = [2, 8, 6, "doron", "doron", "not doron"]
    list2 = [8, 6, "doron", "dont come back"]
    identical_list = identical_occurrence(list1, list2)
    print(identical_list)
