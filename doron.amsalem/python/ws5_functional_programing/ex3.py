def seven_boom_for(num):
    """
    :param number:
    :return list of number according to 7 boom rules:
    """
    ls = []
    for i in range(num+1):
        if i != 0 and i % 7 == 0 or "7" in str(i):
            ls.append("BOOM")
        else:
            ls.append(i)
    return ls

def seven_boom_comprehension(num):
    """
    :param number:
    :return list of number according to 7 boom rules:
    """
    ls = ["BOOM" if i != 0 and (i % 7) == 0 or ("7" in str(i)) else i for i in range(num+1)]
    return ls



def is_boom(a):
    if a != 0 and a % 7 == 0 or "7" in str(a):
        return "BOOM"
    else:
        return a


def seven_boom_map(num):
    """
    :param number:
    :return list of number according to 7 boom rules:
    """
    ls = [i for i in range(num + 1)]
    return list(map(is_boom, ls))



print("seven boom with for", seven_boom_for(73))
print("seven boom with comprehension", seven_boom_comprehension(73))
print("seven boom with map", seven_boom_map(73))
