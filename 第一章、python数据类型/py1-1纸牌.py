import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for rank in self.ranks for suit in self.suits]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


# Python 2.6 开始，namedtuple 就加入到 Python 里，用以构建只有少数属性但是没有方法的对象
# beer_card = Card('7', 'DIAMONDS')
# print(beer_card)
# Card(rank='7', suit='DIAMONDS')
deck = FrenchDeck()
# print(len(deck))
# 52
# print(deck[0])
# print(deck[-1])
from random import choice

# print(choice(deck))
#
# 现在已经可以体会到通过实现特殊方法来利用 Python 数据模型的两个好处。
# 1、作为你的类的用户，他们不必去记住标准操作的各式名称（“怎么得到元素的总数？
# 是 .size() 还是 .length() 还是别的什么？”）。
# 2、可以更加方便地利用 Python 的标准库，比如 random.choice 函数，从而不用重新发明轮子。
# 3、因为 __getitem__ 方法把 [] 操作交给了 self._cards 列表，所以我# 们的 deck 类自
# 动支持切片（slicing）操作。

# print(deck[:3])
# 4、遍历，反向遍历
# for card in deck:
    # print(card)

# for card in reversed(deck):
#     print(card)
# 5、判断是否存在
# print(Card(rank='8', suit='clubs') in deck)
# 6、排序
# 我们按照常规，用点数来判定扑克牌的大小，2 最小、A
# 最大；同时还要加上对花色的判定，黑桃最大、红桃次之、方块再次、
# 梅花最小。下面就是按照这个规则来给扑克牌排序的函数，梅花 2 的大
# 小是 0，黑桃 A 是 51：
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)


def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    print(rank_value,len(suit_values),suit_values[card.suit])
    return rank_value * len(suit_values) + suit_values[card.suit]


for card in sorted(deck, key=spades_high):
    # print(spades_high(card))
    print(card)
# 通过实现 __len__和 __getitem__ 这两个特殊方法，FrenchDeck 就跟一个 Python
# 自有的序列数据类型一样，可以体现出 Python 的核心语言特性（例如迭代和切片）。
# 同时这个类还可以用于标准库中诸如random.choice、reversed 和 sorted 这些函数。
# 另外，对合成的运用使得 __len__ 和 __getitem__ 的具体实现可以代理给 self._cards这个
# Python 列表（即 list 对象）。