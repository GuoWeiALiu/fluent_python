import weakref
>>> s1 = {1, 2, 3}
>>> s2 = s1 ➊
>>> def bye(): ➋
... print('Gone with the wind...')
...
>>> ender = weakref.finalize(s1, bye) ➌
>>> ender.alive ➍
True
>>> del s1
>>> ender.alive ➎
True
>>> s2 = 'spam' ➏
Gone with the wind...
>>> ender.alive
False