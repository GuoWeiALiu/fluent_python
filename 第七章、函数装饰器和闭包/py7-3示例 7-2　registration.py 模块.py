# 装饰器的一个关键特性是，它们在被装饰的函数/定义之后立即运行。这
# 通常是在导入时（即 Python 加载模块时）
register1 = []


def register(func):
    print('running register(%s)' % func)
    register1.append(func)
    return func

@register
def f1():
    print('running fi()')


@register
def f2():
    print('running f2()')

def f3():
    print('running f3()')

def main():
    print('running main()')

    print('register ->, register')

    f1()
    f2()
    f3()
if __name__ == '__main__':
    main()
# ❶ registry 保存被 @register 装饰的函数引用。
# ❷ register 的参数是一个函数。
# ❸ 为了演示，显示被装饰的函数。
# ❹ 把 func 存入 registry。
# ❺ 返回 func：必须返回函数；这里返回的函数与通过参数传入的一
# 样。
# ❻ f1 和 f2 被 @register 装饰。
# ❼ f3 没有装饰。
# ❽ main 显示 registry，然后调用 f1()、f2() 和 f3()。
# ❾ 只有把 registration.py 当作脚本运行时才调用 main()。