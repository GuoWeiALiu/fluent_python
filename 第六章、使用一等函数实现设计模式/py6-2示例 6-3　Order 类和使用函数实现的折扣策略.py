
from collections import namedtuple

from celery.bin.control import inspect

Customer = namedtuple('Customer', 'name fidelity')


class LineItem:
    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price

    def total(self):
        return self.price * self.quantity


class Order:  # 上下文
    def __init__(self, customer, cart, promotion=None):
        self.customer = customer
        self.cart = list(cart)
        self.promotion = promotion

    def total(self):
        if not hasattr(self, '__total'):
            self.__total = sum(item.total() for item in self.cart)

        return self.__total

    def due(self):
        if self.promotion is None:
            discount = 0

        else:
            discount = self.promotion(self)  # ➊计算折扣只需调用 self.promotion() 函数。

        return self.total() - discount

    def __repr__(self):
        fmt = '<Order total: {:.2f} due: {:.2f}>'

        return fmt.format(self.total(), self.due())

    # ➋没有抽象类。


def fidelity_promo(order):
    return order.total() * .05 if order.customer.fidelity >= 1000 else 0

    """➌各个策略都是函数。为积分为1000或以上的顾客提供5%折扣"""


def bulk_item_promo(order):
    """单个商品为20个或以上时提供10%折扣"""

    discount = 0
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * .1
    return discount


def large_order_promo(order):
    """订单中的不同商品达到10个或以上时提供7%折扣"""
    distinct_items = {item.product for item in order.cart}
    if len(distinct_items) >= 10:
        return order.total() * .07
    return 0


joe = Customer('John Doe', 0)
ann = Customer('Ann Smith', 1100)
cart = [LineItem('banana', 4, .5),
        LineItem('apple', 10, 1.5),
        LineItem('watermellon', 5, 5.0)]
Order(joe, cart, fidelity_promo)  # ➋为了把折扣策略应用到 Order 实例上，只需把促销函数作为参数传
# 入。
# <Order total: 42.00 due: 42.00>
Order(ann, cart, fidelity_promo)
# <Order total: 42.00 due: 39.90>
banana_cart = [LineItem('banana', 30, .5), LineItem('apple', 10, 1.5)]
Order(joe, banana_cart, bulk_item_promo)  # ➌
# <Order total: 30.00 due: 28.50>
long_order = [LineItem(str(item_code), 1, 1.0) for item_code in range(10)]
Order(joe, long_order, large_order_promo)
# <Order total: 10.00 due: 9.30>
Order(joe, cart, large_order_promo)
# <Order total: 42.00 due: 42.00>
promos = [fidelity_promo, bulk_item_promo, large_order_promo]


# 6.1.3　选择最佳策略：简单的方式
# ➊promos 列出以函数实现的各个策略。
def best_promo(order):
    return max(promo(order) for promo in promos)


# ➋与其他几个 *_promo 函数一样，best_promo 函数的参数是一个
# Order 实例
"""选择可用的最佳折扣"""

# ➌使用生成器表达式把 order 传给 promos 列表中的各个函数，返回
# 折扣额度最大的那个函数。

# 6.1.4　找出模块中的全部策略

# 虽然示例 6-6 可用，而且易于阅读，但是有些重复可能会导致不易察觉
# 的缺陷：若想添加新的促销策略，要定义相应的函数，还要记得把它添
# 加到 promos 列表中；否则，当新促销函数显式地作为参数传给 Order
# 时，它是可用的，但是 best_promo 不会考虑它。
promos = [globals()[name] for name in globals()
          if name.endswith('_promo')
          and name != 'best_promo']


# ❶ 迭代globals()返回字典中的各个name。
# ❷ 只选择以_promo结尾的名称。
# ❸ 过滤掉best_promo自身，防止无限递归。

def best_promo(order):
    """选择可用的最佳折扣
    """
    return max(promo(order) for promo in promos)


# ❹ best_promo 内部的代码没有变化。

# 示例 6-8　内省单独的 promotions 模块，构建 promos 列表

promos = [func for name, func in inspect.getmembers(promotions, inspect.isfunction)]


def best_promo(order):
    """选择可用的最佳折扣"""
    return max(promo(order) for promo in promos)
