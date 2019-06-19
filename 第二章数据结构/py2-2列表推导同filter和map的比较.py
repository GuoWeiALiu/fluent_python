str = 'qwertyuiop'
code = [ord(i) for i in str if ord(i) > 115]
print(code)
code1 = list(filter(lambda c: c > 115, map(ord, str)))
print(code1)
