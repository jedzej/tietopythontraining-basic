def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


number = int(input("number: "))
if number < 0:
    print("Wrong number.")
else:
    print(fib(number))
