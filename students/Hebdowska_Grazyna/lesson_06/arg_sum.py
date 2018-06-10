def arg_sum(*args):
    suma = 0
    for i in args:
        suma += i
    return suma


print(arg_sum(1, 2, 3, 4))
