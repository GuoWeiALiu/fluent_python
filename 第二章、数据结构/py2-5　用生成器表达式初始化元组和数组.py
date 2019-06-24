str = 'qwertyuiop'
t = tuple(ord(s) for s in str)
print(t)
# 如果生成器表达式是一个函数调用过程中的唯一参数，那么不需要
# 额外再用括号把它围起来。
import array

print(array.array('i', (ord(s) for s in str)))
