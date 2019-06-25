from array import array
import reprlib
import math


class Vector:
    typecode = 'f'

    def __init__(self, components):
        # ❶ self._components是“受保护的”实例属性，把Vector 的分量保存在一个数组中。
        self._components = array(self.typecode, components)

    def __iter__(self):
        # ❷ 为了迭代，我们使用self._components构建一个迭代器。
        return iter(self._components)

    def __repr__(self):
       # 3
        components = reprlib.repr(self._components)
       # 4
        components = components[components.find('['):-1]
        return 'Vector({})'.format(components)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        # 5
        return (bytes[ord(self.typecode)] + \
        bytes(self._components))

    def __eq__(self, other):
        return tuple(self)==tuple(other)

    def __abs__(self):
        # 6
        return math.sqrt(sum(x*x for x in self))

    def __bool__(self):
        return bool(abs(self))

    @classmethod
    def frombytes(cls,octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:].cast(typecode))
        # 7
        return cls(memv)
# ❹ 把字符串插入 Vector 的构造方法调用之前，去掉前面的
# array('d' 和后面的 )。
# ❺ 直接使用 self._components 构建 bytes 对象。
# ❻ 不能使用 hypot 方法了，因此我们先计算各分量的平方之和，然后
# 再使用 sqrt 方法开平方。
# ❼ 我们只需在 Vector2d.frombytes 方法的基础上改动最后一行：直
# 接把 memoryview 传给构造方法，不用像前面那样使用 * 拆包。