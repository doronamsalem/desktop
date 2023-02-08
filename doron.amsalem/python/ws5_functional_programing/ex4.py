def list_to_dict(lis):
    """
    :param list:
    :return dictionary of index and his value:
    """
    indexs_d = {}
    for i in range(len(lis)):
        indexs_d.update({i: lis[i]})
    return indexs_d

print(list_to_dict([1, 2, 3, 4, 5, 6]))


def list_to_dict(lis):
    """
    :param list:
    :return dictionary of index and his value:
    """
    indexs_d = {i: lis[i] for i in range(len(lis))}
    return indexs_d

print(list_to_dict([1, 2, 3, 4, 5, 6, 7]))