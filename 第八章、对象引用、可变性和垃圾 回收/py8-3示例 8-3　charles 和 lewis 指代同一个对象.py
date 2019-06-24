a = {'name': 'Charles L. Dodgson', 'born': 1832}
b= a
print(b is a)
print(id(a), id(b))
# 示例 8-4 实现并测试了图 8-2 中那个 alex 对象。
c = {'name': 'Charles L. Dodgson', 'born': 1832}
print(a==c)
print(c is a)
print(id(c), id(b))