def is_duplicate(list_nums):
    return sum(list_nums) == sum(set(list_nums))


print(is_duplicate([1, 2, 3, 4, 4, 5, 6, 7, 8, 9, 10]))
print(is_duplicate([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
