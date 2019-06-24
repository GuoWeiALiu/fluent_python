from abc import ABC, abstractmethod
from collections import namedtuple

Customer = namedtuple('Customer', 'name fidelity')


class LineItem:
    def __init__(self, product, quantity, price):
        self.product = product
        self.quanlity = quantity
        self.price = price

    def total(self):
        return self.price * self.quanlity


class Order:
    def __init__(self, customer, cart, promotion=None):
        self.customer = customer
        self.cart = cart
        self.promotiom = promotion

    def total(self):
        if not hasattr(self, '__total'):
            self.__total = sum(item.total() for item in self.cart)
        return self.__total

    def due(self):
        if self.promotiom is None:
            discount = 0
        else:
            discount = self.promotiom.discount(self)
        return self.total() - discount

    def __repr__(self):
        fmt = '<Order total: {:.2f} due: {:.2f}>'
        return fmt.format(self.total(), self.due())


class Promotion(ABC):  # 策略：抽象基类
    @abstractmethod
    def discount(self, order):
        """返回折扣金额（正值）"""


class FidelityPromo(Promotion):  # 第一个具体策略

    def discount(self, order):
        return order.total() * .05 if order.customer.fidelity >= 1000 else 0


class BulkItemPromo(Promotion):  # 第二个具体策略

    """单个商品为20个或以上时提供10%折扣"""

    def discount(self, order):

        discount = 0
        for item in order.cart:
            if item.quantity >= 20:
                discount += item.total() * .1
        return discount


class LargeOrderPromo(Promotion):  # 第三个具体策略


    """订单中的不同商品达到10个或以上时提供7%折扣"""


    def discount(self, order):
        distinct_items = {item.product for item in order.cart}
        if len(distinct_items) >= 10:
            return order.total() * .07
        return 0
# ❶ 两个顾客：joe 的积分是 0，ann 的积分是 1100。
joe = Customer('John Doe', 0)
ann = Customer('Ann Smith', 1100)
# ❷ 有三个商品的购物车。
cart = [LineItem('banana', 4, .5),
LineItem('apple', 10, 1.5),
LineItem('watermellon', 5, 5.0)]
# ❸ fidelityPromo 没给 joe 提供折扣。
Order(joe, cart, FidelityPromo())


# ❹ ann 得到了 5% 折扣，因为她的积分超过 1000。
Order(ann, cart, FidelityPromo())
# ❺ banana_cart 中有 30 把香蕉和 10 个苹果。
banana_cart = [LineItem('banana', 30, .5), LineItem('apple', 10, 1.5)]
# ❻ BulkItemPromo 为 joe 购买的香蕉优惠了 1.50 美元。
Order(joe, banana_cart, BulkItemPromo())
# ❼ long_order 中有 10 个不同的商品，每个商品的价格为 1.00 美元。
long_order = [LineItem(str(item_code), 1, 1.0)for item_code in range(10)]
# ❽ LargerOrderPromo 为 joe 的整个订单提供了 7% 折扣。
Order(joe, long_order, LargeOrderPromo())
Order(joe, cart, LargeOrderPromo())