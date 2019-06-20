import bisect
import random
SIZE=7
# seed() 方法改变随机数生成器的种子，可以在调用其他随机模块函数之前调用此函数。。
random.seed(1729)
my_list = []
for i in range(SIZE):
    # randrange()    方法返回指定递增基数集合中的一个随机数，基数缺省值为1。
    new_item = random.randrange(SIZE*2)
    bisect.insort(my_list, new_item)
    print('%2d ->' % new_item, my_list)