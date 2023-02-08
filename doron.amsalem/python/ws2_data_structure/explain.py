#1
a = 1
b = 1
print(a == b, a is b)

#2
a = 55555
b = 55555
print(a == b, a is b)

#3
a = ()
b = ()
print(a == b, a is b)

#4
a = (1, 2, 3)
b = (1, 2, 3)
print(a == b, a is b)

#5
a = []
b = []
print(a == b, a is b)

#6
a = [1, 2, 3]
b = a[:]
print(a == b, a is b)

#7
x = [1, 2, 3]
y = x
y[0] = 8
print(x)

#8 eror!!

#9
x = 1
y = x
y = 2
print(x)

#11
x = 'DevOps'
print(x[-1:-2])
print(x[3:-1])
print(x[::1])
print(x[::3])
print(x[1:2:3])
print(x[::-1])
print(x[1::-1])