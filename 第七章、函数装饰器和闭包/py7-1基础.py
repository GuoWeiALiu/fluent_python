@decorate
def target():
    print('running target()')
# 上述代码的效果与下述写法一样：
def target():
    print('running target()')
target = decorate(target)
# 两种写法的最终结果一样：上述两个代码片段执行完毕后得到的
# target 不一定是原来那个 target 函数，而是 decorate(target) 返
# 回的函数。
