def faction(n):
    ''':returns n!'''
    return 1 if n < 2 else n * faction(n - 1)


print(faction(4))
print(faction.__doc__)
print(type(faction))
fact = faction
# 示例 5-2通过别的名称使用函数，再把函数作为参数传递
print(fact(5))
# map 函数返回一个可迭代对象，里面的元素是把第一个参数（一个函数）应用到第二个参数
print(list(map(fact, range(11))))
# 内置函数 sorted 也是：可选的 key 参数用于提供一个函数，它会应用到各个
# 元素上进行排序
# 示例 5-3　根据单词长度给一个列表排序
fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
print(sorted(fruits, key=len))


# 示例 5-4　根据反向拼写给一个单词列表排序
def reverse(str):
    return str[::-1]


print(reverse('test'))
print(sorted(fruits, key=reverse))
# 示例 5-5　计算阶乘列表：map 和 filter 与列表推导比较
list0 = list(map(fact, range(6)))
list1 = [fact(n) for n in range(6)]
list2 = list(map(fact, filter(lambda n: n % 2, range(6))))
list3 = [faction(n) for n in range(6) if n % 2]
print(list0, list1,list2,  list3)
# Python 中有各种各样可调用的类型，因此判断对象能否调用，最安
# 全的方法是使用内置的 callable() 函数：

print([callable(obj) for obj in (abs, str, 13)])