def deco(func):
    def inner():
        print('running inner()')

    return func


@deco
def target():
    print('running target()')


print(target)
print(target())
