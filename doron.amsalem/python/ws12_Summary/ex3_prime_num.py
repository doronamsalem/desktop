# review by vica
def is_prime(number):
    """gets number\nreturn if number is prime"""
    try:
        prime = True
        if number < 2:
            prime = False
        else:
            for x in range(2, int(number / 2 + 1)):
                if number % x == 0:
                    prime = False
        return prime

    except TypeError:
        raise TypeError("argument must be a number")



if __name__ == '__main__':
    print(is_prime("g"))
    print(is_prime(1))
    print(is_prime(0))
    print(is_prime(7))
