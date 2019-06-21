a = '中国'
b = a.encode('utf8')
print(b)
print(len(b))

print(a)
print(len(a))

c = 'café'
d = c.encode('utf8')
print(d)
print(len(d))
print("------------------------------")
x = b'caf\xc3\xa9'
y = x.decode()
print(y)