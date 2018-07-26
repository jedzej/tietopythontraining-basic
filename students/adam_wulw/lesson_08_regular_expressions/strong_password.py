import re
STRONG_MAX_LEVEL = 3


def patern_match(_str, pattern):
    r = re.compile(r'' + pattern)
    if r.search(_str) is None:
        return False
    return True


def spd(password):
    strong = 0
    if patern_match(password, '\d'):
        strong += 1
    if patern_match(password, '\S{8}'):
        strong += 1
    if patern_match(password, '[A-Z]') and patern_match(password, '[a-z]'):
        strong += 1
    return strong


my_password = 'w8ia#$S1'

if spd(my_password) >= STRONG_MAX_LEVEL:
    print('Password is strong')
else:
    print('Password is weak')
