from collections import deque

# ❶ maxlen 是一个可选参数，代表这个队列可以容纳的元素的数量，而
# 且一旦设定，这个属性就不能修改了。
dq = deque(range(10), maxlen=10)
# ❷ 队列的旋转操作接受一个参数 n，当 n > 0 时，队列的最右边的 n
# 个元素会被移动到队列的左边。当 n < 0 时，最左边的 n 个元素会被
# 移动到右边。
dq.rotate(3)
print(dq)
dq.rotate(-4)
print(dq)

# ❸ 当试图对一个已满（len(d) == d.maxlen）的队列做尾部添加操作
# 的时候，它头部的元素会被删除掉。注意在下一行里，元素 0 被删除
# 了。
dq.appendleft(-1)
print(dq)
# ❹ 在尾部添加 3 个元素的操作会挤掉 -1、1 和 2。
dq.extend([11,22,33])
print(dq)
# ❺ extendleft(iter) 方法会把迭代器里的元素逐个添加到双向队列
# 的左边，因此迭代器里的元素会逆序出现在队列里。
dq.extendleft([10,20,30,40])
print(dq)
