a = (1, 2, [30, 40])
b = (1, 2, [30, 40])
print(a == b)

print(id(a[-1]))

print(a[-1].append(99))
print(a)

print(id(a[-1]))
print(a == b)

x = (1,3)
y =(3,4)
print(x+y, x, y)