s1 = 'café'
s2 = 'cafe\u0301'
print(s1, s2)
# ('café', 'café')
print(len(s1), len(s2))
# (4, 5)
print(s1 == s2)
# False

from unicodedata import normalize
s1 = 'café' # 把"e"和重音符组合在一起
s2 = 'cafe\u0301' # 分解成"e"和重音符
print(len(s1), len(s2))
# (4, 5)
print(len(normalize('NFC', s1)), len(normalize('NFC', s2)))
# (4, 4)
print(len(normalize('NFD', s1)), len(normalize('NFD', s2)))
# (5, 5)
print(normalize('NFC', s1) == normalize('NFC', s2))
print(normalize('NFD', s1) == normalize('NFD', s2))