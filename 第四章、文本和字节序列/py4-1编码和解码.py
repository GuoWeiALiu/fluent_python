# ❶ 'café' 字符串有 4 个 Unicode 字符。
s = 'café'
print(len(s))
# ❷ 使用 UTF-8 把 str 对象编码成 bytes 对象。
b = s.encode('utf8')
print(b)
# ❸ bytes 字面量以 b 开头。

# ❹ 字节序列 b 有 5 个字节（在 UTF-8 中，“é”的码位编码成两个字
# 节）。
print(len(b))
# ❺ 使用 UTF-8 把 bytes 对象解码成 str 对象。
c = b.decode('utf8')
print(c)