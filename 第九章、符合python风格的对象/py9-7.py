

from array import array
import math

# BEGIN VECTOR2D_V3_PROP
class Vector2d:
    typecode = 'd'

    def __init__(self, x, y):
        self.__x = float(x)  # <1>
        self.__y = float(y)

    @property  # <2>
    def x(self):  # <3>
        return self.__x  # <4>

    @property  # <5>
    def y(self):
        return self.__y

    def __iter__(self):
        return (i for i in (self.x, self.y))  # <6>

    # remaining methods follow (omitted in book listing)
# END VECTOR2D_V3_PROP

    def __repr__(self):
        class_name = type(self).__name__
        return '{}({!r}, {!r})'.format(class_name, *self)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) +
                bytes(array(self.typecode, self)))

    def __eq__(self, other):
        return tuple(self) == tuple(other)

# BEGIN VECTOR_V3_HASH
    def __hash__(self):
        return hash(self.x) ^ hash(self.y)
# END VECTOR_V3_HASH

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

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

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(*memv)

v1 = Vector2d(3.0, 4.0)
# BEGIN VECTOR2D_V3_DEMO
#Tests of `x` and `y` read-only properties:
print(v1.x, v1.y)

    # >>> v1.x = 123
    # Traceback (most recent call last):
    #   ...
    # AttributeError: can't set attribute
# END VECTOR2D_V3_HASH_DEMO
# Tests of hashing:
# BEGIN VECTOR2D_V3_HASH_DEMO
v1 = Vector2d(3, 4)
v2 = Vector2d(3.1, 4.2)
print(hash(v1), hash(v2))
    # (7, 384307168202284039)
print(len(set([v1, v2])))

# END VECTOR2D_V3_DEMO
print(v1.__dict__)
print(v1._Vector2d__x)