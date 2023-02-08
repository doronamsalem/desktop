class X(object):

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def foo(self, a):
        self.c = a


r = X(1, "hello")
print(r.a, r.b)
print(type(r), "\n")
# qu 9
r.foo(6)
print(r.c)
# qu 10
r.z = 42
print(r.z)
