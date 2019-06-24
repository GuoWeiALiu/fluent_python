from functools import singledispatch
from collections import abc
import numbers
import html


# ➊@singledispatch 标记处理 object 类型的基函数。
@singledispatch
def htmlize(obj):
    content = html.escape(repr(obj))
    return '<pre>{}</pre>'.format(content)
@htmlize.register(str)
def _(text):
# ➋各个专门函数使用 @«base_function».register(«type») 装饰。
# ➌专门函数的名称无关紧要；_ 是个不错的选择，简单明了。
    content = html.escape(text).replace('\n', '<br>\n')
    return '<p>{0}</p>'.format(content)
@htmlize.register(numbers.Integral)
# ➍❹ 为每个需要特殊处理的类型注册一个函数。numbers.Integral 是
# int 的虚拟超类。
def _(n):
    return '<pre>{0} (0x{0:x})</pre>'.format(n)


@htmlize.register(tuple)

# ➎可以叠放多个 register 装饰器，让同一个函数支持不同类型。

@htmlize.register(abc.MutableSequence)
def _(seq):
    inner = '</li>\n<li>'.join(htmlize(item) for item in seq)
    return '<ul>\n<li>' + inner + '</li>\n</ul>'
print(htmlize({1,2,3}))
print(htmlize(abs))
print(htmlize('Heimlich & Co.\n- a game'))
print(htmlize(42))
print(htmlize(['alpha',66,{3,2,1}]))