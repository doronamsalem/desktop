def sum_of_divisors(num):
    """return the sum of divisors for given num"""
    sum = 0
    for x in range(1, num + 1):
        if num % x == 0:
            sum += x
    return sum


print(sum_of_divisors(5))