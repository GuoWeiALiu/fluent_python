# ❶ 从文本文件里读取 1000 万个浮点数。
import numpy
from array import array
from random import random

floats = array('d', (random() for i in range(10 ** 2)))
numpy.savetxt('C:/my file/03.python/中级书籍/fluent_python/第二章、数据结构/filename3.txt', floats)
numpy.loadtxt()

# ❷ 利用序列切片来读取其中的最后 3 个数。
# ❸ 把数组里的每个数都乘以 0.5，然后再看看最后 3 个数。
# ❹ 导入精度和性能都比较高的计时器（Python 3.3 及更新的版本中都有
# 这个库）。
# ❺ 把每个元素都除以 3，可以看到处理 1000 万个浮点数所需的时间还
# 不足 40 毫秒。
# ❻ 把数组存入后缀为 .npy 的二进制文件。
# ❼ 将上面的数据导入到另外一个数组里，这次 load 方法利用了一种叫
# 作内存映射的机制，它让我们在内存不足的情况下仍然可以对数组做切
# 片。
# ❽ 把数组里每个数乘以 6 之后，再检视一下数组的最后 3 个数。