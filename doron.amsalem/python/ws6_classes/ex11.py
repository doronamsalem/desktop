class B(object):
    def foo(self):
        return "B"


class D(B):
    pass

b = B()
d = D()

print(b.foo())
print(d.foo())
