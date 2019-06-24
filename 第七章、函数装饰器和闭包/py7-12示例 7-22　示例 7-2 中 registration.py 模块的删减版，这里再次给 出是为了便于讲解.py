registry = []


def register(func):
    print('running register(%s)' % func)
    registry.append(func)
    return func


@register
def f1():
    print('running f1()')
    print('running main()')
    print('registry ->', registry)


f1()
registry = set()
# registry 现在是一个 set 对象，这样添加和删除函数的速度更快。
# register 接受一个可选的关键字参数。
def register(active=True):
    # ❸ decorate这个内部函数是真正的装饰器；注意，它的参数是一个函    数。
    def decorate(func):
        print('running register(active=%s)->decorate(%s)'% (active, func))
        if active:
            registry.add(func)
            # 只有 active  参数的值（从闭包中获取）是 True  时才注册 func。
        else:
            registry.discard(func)
        return func
    return decorate

@register(active=False)
def f1():
    print('running f1()')
@register()
def f2():
    print('running f2()')
def f3():
    print('running f3()')
# ❺ 如果 active 不为真，而且 func 在 registry 中，那么把它删除。❻ decorate 是装饰器，必须返回一个函数。
# ❼ register 是装饰器工厂函数，因此返回 decorate。
# ❽ @register 工厂函数必须作为函数调用，并且传入所需的参数。
# ❾ 即使不传入参数，register 也必须作为函数调用
# 书籍下载qq群6089740 钉钉群21734177 IT书籍 http://t.cn/RDIAj5D
# 电子