import re


def my_strip(*args):
    if len(args) > 1:
        f = str(args[1])
    else:
        f = ' '
    r = re.compile(r'[^' + f + ' ].*[^' + f + ']')
    mo = r.search(args[0])
    print("{" + mo.group() + "}")
    return mo


my_strip('aa bb xx', 'a')
