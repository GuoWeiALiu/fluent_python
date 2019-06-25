print(slice)
print(dir(slice))
print(help(slice.indices))
s = 'ABCDE'
x = slice(None, 10, 2).indices(5)
y = slice(-3, None, None).indices(5)
print(x, y)
# 'ABCDE'[:10:2] 等同于 'ABCDE'[0:5:2]
# 'ABCDE'[-3:] 等同于 'ABCDE'[2:5:1]
