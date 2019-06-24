import collections
ct = collections.Counter('qwertrewqsdertdfgt')
print(ct)
ct.update('qqqwe')
print(ct)
a = ct.most_common(3)
print(a)