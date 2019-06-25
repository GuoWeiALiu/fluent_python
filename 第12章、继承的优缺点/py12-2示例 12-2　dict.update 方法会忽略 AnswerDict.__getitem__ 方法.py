class AnswerDict(dict):
    def __getitem__(self, item):
        return 42
ad = AnswerDict(a='foo')
print(ad['a'])
d = {}
d.update(ad)
print(d['a'])
print(d)
# 42
# foo
# {'a': 'foo'}

# ❶ 不管传入什么键，AnswerDict.__getitem__ 方法始终返回 42。
# ❷ ad 是 AnswerDict 的实例，以 ('a', 'foo') 键值对初始化。
# ❸ ad['a'] 返回 42，这与预期相符。
# ❹ d 是 dict 的实例，使用 ad 中的值更新 d。
# ❺ dict.update 方法忽略了 AnswerDict.__getitem__ 方法。