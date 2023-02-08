def foo1(n):
    n = 4
    print('n in foo1', n)
    return n


def foo2(n):
    n[0] = 4
    print(n)

n = [3]
foo2(n)
print(n, "\n")


def foo3(n):
    n[0] = 4
    print(n)

n = (3,)
# foo3(n)    makes an error, tuple immutable
print(n, "\n")


def foo4():
    if x == 42:
        print("x is 42\n")
    else:
        print("x is not 42\n")

x = 42
foo4()


def foo5(a = []):
    a.append(1)
    print(a, "\n")

foo5()
foo5()

if __name__ == "__main__":
    n = 3
    foo1(n)
    print("after foo1 in main", n, "\n")


