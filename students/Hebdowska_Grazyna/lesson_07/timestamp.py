import time


def conwert_time(t):
    new_t = time.localtime(t)
    y = new_t[0]
    m = new_t[1]
    d = new_t[2]
    print(y, m, d)


t = float(input())
conwert_time(t)
