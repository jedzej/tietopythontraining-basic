def sum_all(*nums):
    _sum = 0
    for num in nums:
        _sum = _sum + num
    return _sum


def inspect_args(*args):
    i = 0
    for arg in args:
        i = i + 1
        print("%d. arg type: %s, value " % (i, type(arg)), arg)


def inspect_kwards(**kwargs):
    i = 0
    for v, k in kwargs.items():
        i = i + 1
        print("%d. value: %s, key %s" % (i, k, v))


def foo(*args, **kwargs):
    print('foo args', args)
    print('foo kwargs', kwargs)


def logger_wrapper(foo, *args, **kwargs):
    print('args: ')
    inspect_args(*args)
    print('kwargs: ')
    inspect_kwards(**kwargs)
    foo(*args, **kwargs)


print('========sum_all========')
print('sum_all = ', sum_all(1, 2, 3))
print('========inspect_args========')
inspect_args(1, 2, 'text', {1, 2}, [3, 4], (5, 6), {'value': '1'})
print('========logger_wrapper========')
logger_wrapper(foo, 1, 3, 4, 'my text', a=2, b=3)
