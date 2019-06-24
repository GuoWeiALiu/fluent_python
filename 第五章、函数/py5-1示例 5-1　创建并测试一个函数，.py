def faction(n):
    ''':returns n!'''
    return 1 if n < 2 else n * faction(n - 1)
print(faction(4))
print(faction.__doc__)
print(type(faction))
