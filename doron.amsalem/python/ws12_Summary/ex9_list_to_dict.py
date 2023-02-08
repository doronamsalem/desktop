# review by vica

# with comprehension
def list_to_dict(ls):
    """create dictionary from list with index as key"""
    assert type(ls) is list
    return {ind: ls[ind] for ind in range(len(ls))}


# without comprehension
def list_to_dict1(ls):
    """create dictionary from list with index as key"""
    assert type(ls) is list
    dictionary = {}
    for ind in range(len(ls)):
        dictionary.update({ind: ls[ind]})
    return dictionary


if __name__ == "__main__":
    l = ['a', 'b', 'c', 8]
    print(list_to_dict(l))
    print(list_to_dict1(l))