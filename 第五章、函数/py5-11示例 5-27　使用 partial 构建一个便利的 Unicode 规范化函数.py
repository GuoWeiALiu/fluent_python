import unicodedata, functools
nfc = functools.partial(unicodedata.normalize,'NFC')
s1 = 'café'
s2 = 'cafe\u0301'
print(s1==s2)
print(nfc(s1)==nfc(s2))
# partial 的第一个参数是一个可调用对象，后面跟着任意个要绑定的定
# 位参数和关键字参数。