b=6
def f1(a):
    print(a)
    global b
    b =9
    print(b)
f1(3)
