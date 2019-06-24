def make_averager():
    count = 0
    total = 0
    def averager(new_value):
        nonlocal count, total
        count += 1
        total += new_value
        return total / count
    return averager
avg = make_averager()
print(avg(10))
# UnboundLocalError: local variable 'count' referenced before assignment

# 但是对数字、字符串、元组等不可变类型来说，只能读取，不能更新。
# 如果尝试重新绑定，例如 count = count + 1，其实会隐式创建局部
# 变量 count。这样，count 就不是自由变量了，因此不会保存在闭包
# 中。
# 加入nonlocal