import array

numbers = array.array('h',[-2,-1,0,1,2])
memv = memoryview(numbers)
print(len(memv))
print(memv.tolist())
# ❸ 创建一个 memv_oct，这一次是把 memv 里的内容转换成 'B' 类型，
# 也就是无符号字符。
memv_oct = memv.cast('B')
print(memv_oct.tolist())
# 因为我们把占 2 个字节的整数的高位字节改成了 4，所以这个有符号
# 整数的值就变成了 1024。
memv_oct[5] =4
print(numbers)