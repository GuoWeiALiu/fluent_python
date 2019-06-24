import time
import functools

def clock(func):
    def clocked(*args):
        t0 = time.perf_counter()
        result = func(*args)
        elapsed = time.perf_counter() - t0
        name = func.__name__
        args_str = ','.join(repr(arg) for arg in args)
        print('[%0.8fs]%s(%s)->%r' % (elapsed, name, args_str, result))
        return result

    return clocked
@functools.lru_cache() #
# ❶ 注意，必须像常规函数那样调用 lru_cache。这一行中有一对括
# 号：@functools.lru_cache()。这么做的原因是，lru_cache 可以
# 接受配置参数，稍后说明。
@clock
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 2) + fibonacci(n - 1)


print(fibonacci(6))
