x = [1,2,3]
y = x
y[0] = 0
z = x.copy()
print(x)
print(y)
print(z)
print(hex(id(x)))
print(hex(id(y)))
print(hex(id(z)))
