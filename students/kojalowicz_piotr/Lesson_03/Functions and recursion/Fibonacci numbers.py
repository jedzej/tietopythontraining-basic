def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


correctInPut = None
while correctInPut is None:
    try:
        n = int(input())
        if n >= 0:
            print(fib(n))
            correctInPut = 1
        else:
            print('The number must integer biger then -1')
    except ValueError:
        print('The number must integer biger then -1')
