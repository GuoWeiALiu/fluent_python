lax_co = (33, -118)
x, y = lax_co
print(x)
print(y)
# 用 * 运算符把一个可迭代对象拆开作为函数的参数：
print(divmod(20, 8))
t = (20, 8)
print(divmod(*t))
a, b = divmod(*t)
print(a, b)

import os
_, filename = os.path.split('/home/lgw/1.txt')
print(filename)

a,b,*c = range(11)
print(c)
a, *c , b = range(11)
print(c)