def tags(name, *content, cls=None, **attrs):
    """生成一个或多个HTML标签"""
    if cls is not None:
        attrs['class'] = cls

    if attrs:
        attrs_str = ''.join('%s = "%s"' % (attr, value) for attr, value in sorted(attrs.items()))
    else:
        attrs_str = ''
    if content:
        return "\n".join('<%s%s>%s<%s>' % (name, attrs_str, c, name) for c in content)
    else:
        return "<%s%s/ >" % (name, attrs_str)
print(tags)
from functools import partial
picture = partial(tags, 'img', cls = 'pic-frame')
print(picture(src='www.baidu.com'))
print(picture)
print(picture.func)
print(picture.args)
print(picture.keywords)
# 从示例 5-10 中导入 tag 函数，查看它的 ID。
# ❷ 使用 tag 创建 picture 函数，把第一个定位参数固定为 'img'，把
# cls 关键字参数固定为 'pic-frame'。
# ❸ picture 的行为符合预期。
# ❹ partial() 返回一个 functools.partial 对象。
# functools.py 的源码（https://hg.python.org/cpython/file/default/Lib/functools.py）表
# 明，functools.partial 类是使用 C 语言实现的，而且默认使用这个实现。如果这个实现不
# 可用，从 Python 3.4 起，functools 模块为 partial 提供了纯 Python 实现。
# ❺ functools.partial 对象提供了访问原函数和固定参数的属性。