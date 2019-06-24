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


# ❶ promos 列表起初是空的。
promos = []


# ❷ promotion 把 promo_func 添加到 promos 列表中，然后原封不动
# 地将其返回。
def promotion(promo_func):
    promos.append(promo_func)
    return promo_func


@promotion
def fidelity_promo(order):
    return order.total() * .05 if order.customer.fidelity >= 1000 else 0

    """➌各个策略都是函数。为积分为1000或以上的顾客提供5%折扣"""


@promotion
def bulk_item_promo(order):
    """单个商品为20个或以上时提供10%折扣"""

    discount = 0
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * .1
    return discount

# ❸ 被 @promotion 装饰的函数都会添加到 promos 列表中。
@promotion
def large_order_promo(order):
    """订单中的不同商品达到10个或以上时提供7%折扣"""
    distinct_items = {item.product for item in order.cart}
    if len(distinct_items) >= 10:
        return order.total() * .07
    return 0
# ❹ best_promos 无需修改，因为它依赖 promos 列表。
def best_promo(order):
    """选择可用的最佳折扣"""
    return max(promo(order) for promo in promos)