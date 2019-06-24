from types import MappingProxyType

D = {1: 'A'}
d_proxy = MappingProxyType(D)
print(d_proxy)
# ➊ d 中的内容可以通过 d_proxy 看到。

# ➋ 但是通过 d_proxy 并不能做任何修改。

d_proxy[2] = 'x'
# baocuo
#     d_proxy[2] = 'x'
# TypeError: 'mappingproxy' object does not support item assignment

# ➌ d_proxy 是动态的，也就是说对 d 所做的任何改动都会反馈到它上
# 面。
D[2] = 'X'
print(d_proxy)
