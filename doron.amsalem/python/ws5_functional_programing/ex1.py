from functools import reduce

ls = (1, 3, 5, 6)
def sum_for(lis):
    """
    :param list of numbers:
    :return sum of all numbers:
    """
    sum = 0
    for i in lis:
        sum += i
    print("with for", sum)

sum_for(ls)

def sum_a_b(a, b):
    return a + b
def list_sum(ls):
    return(reduce(sum_a_b, ls))

print("with reduce", list_sum(ls))


print("with sum", sum(ls))


