>>> import weakref
>>> a_set = {0, 1}
>>> wref = weakref.ref(a_set) ➊
>>> wref
<weakref at 0x100637598; to 'set' at 0x100636748>
>>> wref() ➋
{0, 1}
>>> a_set = {2, 3, 4} ➌
>>> wref() ➍
{0, 1}
>>> wref() is None ➎
False
>>> wref() is None ➏
True