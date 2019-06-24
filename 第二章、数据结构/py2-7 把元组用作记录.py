lax_co = (33, -118)
city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)
traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]

for passport in sorted(traveler_ids):
    print('%s/%s' % passport)

for country, _ in traveler_ids:
    print(country)
# for 循环可以分别提取元组里的元素，也叫作拆包（unpacking）。因
# 为元组中第二个元素对我们没有什么用，所以它赋值给“_”占位符。