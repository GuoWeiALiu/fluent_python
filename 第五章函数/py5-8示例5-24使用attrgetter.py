from collections import namedtuple

metro_data = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]
from collections import namedtuple

LatLong = namedtuple('LatLong', 'lat long')  # ➊
Metropolis = namedtuple('Metropolis', 'name cc pop coord')  # ➋
metro_areas = [Metropolis(name, cc, pop, LatLong(lat, long))  # ➌
               for name, cc, pop, (lat, long) in metro_data]
print(metro_areas[0])
Metropolis(name='Tokyo', cc='JP', pop=36.933, coord=LatLong(lat=35.689722,
                                                            long=139.691667))
print(metro_areas[0].coord.lat)  # ➍

from operator import attrgetter

name_lat = attrgetter('name', 'coord.lat')  # ➎
for city in sorted(metro_areas, key=attrgetter('coord.lat')):  # ➏
    print(name_lat(city))  # ➐
# ❶ 使用 namedtuple 定义 LatLong。
# ❷ 再定义 Metropolis。
# ❸ 使用 Metropolis 实例构建 metro_areas 列表；注意，我们使用嵌
# 套的元组拆包提取 (lat, long)，然后使用它们构建 LatLong，作为
# Metropolis 的 coord 属性。
# ❹ 深入 metro_areas[0]，获取它的纬度。
# ❺ 定义一个 attrgetter，获取 name 属性和嵌套的 coord.lat 属性。
# ❻ 再次使用 attrgetter，按照纬度排序城市列表。
# ❼ 使用标号❺中定义的 attrgetter，只显示城市名和纬度。
