a = [10, 20]
b = [a, 30]
a.append(b)
print(a)
# [10, 20, [[...], 30]]
from copy import deepcopy
c = deepcopy(a)
print(c)
# [10, 20, [[...], 30]]