import ws2_data_structure as ws2

if __name__ == "__main__":
    print("ex1 test:")
    ls = [3, 5, "doron", 5, "doron", "amsalem", 4, "infinity", 0]
    ws2.ex1.only_str(ls)
    print(ls)

    print("\nex2 test:")
    print(ws2.occurrence("abbcccdddd"))

    print("\nex3 test:")
    list1 = [2, 8, 6, "doron", "not doron"]
    list2 = [8, 6, "doron", "dont come back"]
    identical_list = ws2.identical_occurrence(list1, list2)
    print(identical_list)

    print("\nex4 test:")
    d = {"a": 3, "b": 4, "c": 4, "d": 5}
    ws2.unique_value(d)

    print("\nex5 test:")
    ls = [1, 2, 3, 4, 5]
    ws2.rotate_left(ls)
    print(ls)

    print("\nex5 test:")
    lis = [1, 2, 3, 4, 5]
    ws2.every_second(lis)

    print("\nex7 test:")
    d = {"a": 1, "b": 2, "c": 3}
    ls = ws2.dict_to_list(d)
    print(ls)

    print("\nex8 test:")
    d = {"a": 1, "b": 2, "c": 3}
    ws2.max_min_dictionary(d)
