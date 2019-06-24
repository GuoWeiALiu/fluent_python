from collections import namedtuple
City = namedtuple('City', 'name country population coordinates')
tokyo = City('tokyo','jp',36.993,(35.689722,139.691722))
print(tokyo)
print(tokyo.population)
print(tokyo[0])
# 具名元组的属性和方法
# _fields属性是一个包含这个类所有字段名称的元组
print(City._fields)
# 用 _make() 通过接受一个可迭代对象来生成这个类的一个实例， 它
# 的作用跟 City(*delhi_data) 是一样的。
LatLong = namedtuple('LatLong', 'lat long')
delhi_data = ('Delhi NCR', 'IN', 21.935, LatLong(28.613889, 77.208889))
delhi = City._make(delhi_data)
print(delhi)
# asdict() 把具名元组以 collections.OrderedDict 的形式返
# 回， 我们可以利用它来把元组里的信息友好地呈现出来。
print(delhi._asdict())