>>> t1 = (1, 2, 3)
>>> t2 = tuple(t1)
>>> t2 is t1 ➊
True
>>> t3 = t1[:]
>>> t3 is t1 ➋
True
>>> t1 = (1, 2, 3)
>>> t3 = (1, 2, 3) # ➊
>>> t3 is t1 # ➋
False
>>> s1 = 'ABC'
>>> s2 = 'ABC' # ➌
>>> s2 is s1 # ➍
True