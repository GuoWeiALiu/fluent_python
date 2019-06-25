class DoppeDict(dict):
    def __setitem__(self, key, value):

        super().__setitem__(key, [value] * 2)


dd = DoppeDict(one=1)
print(dd)
dd['two'] = 2
print(dd)
dd.update(three=3)
print(dd)
# {'one': 1}
# {'one': 1, 'two': [2, 2]}
# {'one': 1, 'two': [2, 2], 'three': 3}
# ❶ DoppelDict.__setitem__ 方法会重复存入的值（只是为了提供易
# 于观察的效果）。它把职责委托给超类。
# ❷ 继承自 dict 的 __init__ 方法显然忽略了我们覆盖的 __setitem__
# 方法：'one' 的值没有重复。
# ❸ [] 运算符会调用我们覆盖的 __setitem__ 方法，按预期那样工
# 作：'two' 对应的是两个重复的值，即 [2, 2]。
# ❹ 继承自 dict 的 update 方法也不使用我们覆盖的 __setitem__ 方
# 法：'three' 的值没有重复。