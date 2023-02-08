def is_palindrom(num):
    return str(num) == str(num)[::-1]

print(is_palindrom(123454321))
