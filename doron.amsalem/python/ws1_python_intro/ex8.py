def prime(num):
    """return is number is prime"""
    for x in range(2, int(num)):
        if int(num) % x == 0:
            return False
    return True


a = input("enter number: ")
if prime(a):
    print("prime")
else:
    print("not prime")