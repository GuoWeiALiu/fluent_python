import random


class BingoCage:
    def __init__(self, items):
        # ❶ __init__
        # 接受任何可迭代对象；在本地构建一个副本，防止列表参
        # 数的意外副作用。
        self._items = list(items)
        # ❷ shuffle定能完成工作，因为self._items是列表。
        random.shuffle(self._items)
        # 起主要作用的方法。
    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            # 如果self._items  # 为空，抛出异常，并设定错误消息。
            return LookupError('pick from empty BingoCage')

    def __call__(self, *args, **kwargs):
        # bingo.pick()的快捷方式是bingo()。
        return self.pick()


bingo = BingoCage(range(6))
print(bingo.pick())
print(bingo())
print(callable(bingo))
