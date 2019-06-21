import struct
fmt = '<3s3sHH'
with open('f.gif','rb') as fp:
    img = memoryview(fp.read())
header = img[:10]
print(bytes(header))
print(struct.unpack(fmt, header))
del header
del img
# 结构体的格式：< 是小字节序，3s3s 是两个 3 字节序列，HH 是两个
# 16 位二进制整数。
# ❷ 使用内存中的文件内容创建一个 memoryview 对象……
# ❸ ……然后使用它的切片再创建一个 memoryview 对象；这里不会复
# 制字节序列。
# ❹ 转换成字节序列，这只是为了显示；这里复制了 10 字节。
# ❺ 拆包 memoryview 对象，得到一个元组，包含类型、版本、宽度和
# 高度。
# ❻ 删除引用，释放 memoryview 实例所占的内存