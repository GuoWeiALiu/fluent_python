from array import array
from random import random

floats = array('d', (random() for i in range(10 ** 7)))
print(floats[-1])
fp = open('floats.bin', 'wb')
# 把数组存入一个二进制文件里。
floats.tofile(fp)
fp.close()
float2 = array('d')
fp = open('floats.bin', 'rb')
# 把 1000 万个浮点数从二进制文件里读取出来。
float2.fromfile(fp, 10 ** 7)
fp.close()
print(float2[-1])
print(floats == float2)
