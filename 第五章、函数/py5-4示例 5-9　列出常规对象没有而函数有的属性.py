class C: pass
obj = C()
def func():pass
a = sorted(set(dir(func))-set(dir(obj)))
print(a)
