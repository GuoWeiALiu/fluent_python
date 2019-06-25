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

    shortcut_names = 'xyzt'
    def __getitem__(self, name):
        cls = type(self)
        if len(name) == 1:
            pos = cls.shortcut_names.find(name)
            if 0<=pos< len(self._components):
                return self._components[pos]
        msg = '{.__name__!r} object has no attribute{!r}'
        raise AttributeError(msg.format(cls,name))

    def __setattr__(self, name, value):
        cls = type(self)

        if len(name) == 1:
            if name in cls.shortcut_names:
                error = 'readonly attribute {attr_name!r}'
            elif name.islower():
                error = "can't set attributes 'a' to 'z' in {cls_name!r}"
            else:
                error = ''
            if error:
                msg = error.format(cls_name=cls.__name__, attr_name=name)
                raise AttributeError(msg)
            super().__setattr__(name, value)

v1= Vector(range(10))
# print(v1.x)
v1.X = 'albatross'
print(v1.X)
v1.ni = 'Ni!'
# print(v1.ni)
v1.x = 7
print(v1.x)