from functools import reduce


def fact(n):
    return reduce(lambda a, b: a * b, range(1, n + 1))


from operator import mul


def fact1(n):
    return reduce(mul, range(1, n + 1))


print(fact1(3))
print(fact(3))
