import math
from array import array


class Vector2d:
    typecode = 'd'  # <1># ❶ typecode 是类属性，在 Vector2d 实例和字节序列之间转换时使用。

    def __init__(self, x, y):
        # ❷ 在 __init__ 方法中把 x 和 y 转换成浮点数，尽早捕获错误，以防
        # 调用 Vector2d 函数时传入不当参数。
        self.x = float(x)  # <2>
        self.y = float(y)

    def __iter__(self):
        # ❸ 定义 __iter__ 方法，把 Vector2d 实例变成可迭代的对象，这样才
        # 能拆包（例如，x, y = my_vector）。这个方法的实现方式很简单，
        # 直接调用生成器表达式一个接一个产出分量。
        # 这一行也可以写成 yield self.x; yield.self.y。第 14 章会进一步讨论 __iter__ 特殊方
        # 法、生成器表达式和 yield 关键字。
        return (i for i in (self.x, self.y))  # <3>

    def __repr__(self):
        class_name = type(self).__name__
        # ❹ __repr__ 方法使用 {!r} 获取各个分量的表示形式，然后插值，构
        # 成一个字符串；因为 Vector2d 实例是可迭代的对象，所以 *self 会把
        # x 和 y 分量提供给 format 函数。
        return '{}({!r}, {!r})'.format(class_name, *self)  # <4>

    def __str__(self):
        # ❺ 从可迭代的 Vector2d 实例中可以轻松地得到一个元组，显示为一个
        # 有序对。
        return str(tuple(self))  # <5>

    def __bytes__(self):
        # ❻ 为了生成字节序列，我们把 typecode 转换成字节序列，然后……
        return (bytes([ord(self.typecode)]) +  # <6>
                bytes(array(self.typecode, self)))  # <7>

    # ❼ ……迭代 Vector2d 实例，得到一个数组，再把数组转换成字节序
    # 列。
    def __eq__(self, other):
        # ❽ 为了快速比较所有分量，在操作数中构建元组。对 Vector2d 实例来
        # 说，可以这样做，不过仍有问题。参见下面的警告。
        return tuple(self) == tuple(other)  # <8>

    def __abs__(self):
        # ❾ 模是 x 和 y 分量构成的直角三角形的斜边长。
        return math.hypot(self.x, self.y)  # <9>

    def __bool__(self):
        # ❿ __bool__ 方法使用 abs(self) 计算模，然后把结果转换成布尔
        # 值，因此，0.0 是 False，非零值是 True。
        return bool(abs(self))  # <10>

    # 类方法使用 classmethod 装饰器修饰
    # @classmethod
    # 不用传入 self 参数；相反，要通过 cls 传入类本身。
    # def frombytes(cls, octets):
    #     # 从第一个字节中读取 typecode。
    #     typecode = chr(octets[0])
    #     # 使用传入的 octets 字节序列创建一个 memoryview，然后使用
    #     # typecode 转换。
    #     memv = memoryview(octets[1:]).cast(typecode)
    #     # ❺ 拆包转换后的 memoryview，得到构造方法所需的一对参数。
    #     return cls(*memv)
    def angle(self):
        return math.atan2(self.y, self.x)

    def __format__(self, fmt_spec=''):
        if fmt_spec.endswith('p'):
            fmt_spec = fmt_spec[:-1]
            coords = (abs(self), self.angle())
            outer_fmt = '<{}, {}>'
        else:
            coords = self
            outer_fmt = '({}, {})'
        components = (format(c, fmt_spec) for c in coords)
        return outer_fmt.format(*components)
v1 = Vector2d(3.0,4.0)
print(format(Vector2d(1, 1), 'p'))
print(format(Vector2d(1, 1), '.3ep'))
print(format(Vector2d(1, 1), '0.5fp'))