class Cheese:


    def __init__(self, kind):


        self.kind = kind


def __repr__(self):


    return 'Cheese(%r)' % self.kind
>>> import weakref
>>> stock = weakref.WeakValueDictionary() ➊
>>> catalog = [Cheese('Red Leicester'), Cheese('Tilsit'),
... Cheese('Brie'), Cheese('Parmesan')]
...
>>> for cheese in catalog:
... stock[cheese.kind] = cheese ➋
>>> sorted(stock.keys())
['Brie', 'Parmesan', 'Red Leicester', 'Tilsit'] ➌
>>> del catalog
>>> sorted(stock.keys())
['Parmesan'] ➍
>>> del cheese
>>> sorted(stock.keys())
[]