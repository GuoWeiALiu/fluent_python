class Averger():
    def __init__(self):
        self.series = []

    def __call__(self, new_value):
        self.series.append(new_value)
        total = sum(self.series)
        return total / len(self.series)


avg = Averger()
print(avg(10))
print(avg(11))
print(avg(12))


def make_avg():
    series = []

    def averager(a):
        series.append(a)
        total = sum(series)
        return total / len(series)

    return averager
avg1 = make_avg()
print(avg1(10))
print(avg1(11))
print(avg1(12))

# 示例 7-11　审查 make_averager（见示例 7-9）创建的函数
print(avg1.__code__.co_varnames)
print(avg1.__code__.co_freevars)
# 示例 7-12　接续示例 7-11
print(avg1.__code__.co_freevars)
print(avg1.__closure__)
print(avg1.__closure__[0].cell_contents)
# series 的绑定在返回的 avg 函数的 __closure__ 属性
# 中。avg.__closure__ 中的各个元素对应于
# avg.__code__.co_freevars 中的一个名称。这些元素是 cell 对象，
# 有个 cell_contents 属性，保存着真正的值。这些属性的值如示例 7-
# 12 所示。