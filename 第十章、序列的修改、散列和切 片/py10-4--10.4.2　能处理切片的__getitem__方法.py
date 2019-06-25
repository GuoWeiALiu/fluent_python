import numbers
from array import array
import reprlib
import math


class Vector:
    typecode = 'd'

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

    def __len__(self):
        return len(self._components)

    def __getitem__(self, index):
       cls = type(self)
       if isinstance(index,slice):
           return cls(self._components[index])
       elif isinstance(index, numbers.Integral):
           return self._components[index]
       else:
           msg = '{cls.__name__}indices must be integers'
           raise TypeError(msg.format(cls=cls))

v1= Vector(range(10))
print(v1[-1])
print(v1[1:4])
print(v1[-1:])
# Vector 不支持多维索引，因此索引元组或多个切片会抛出错
print(v1[1,2])