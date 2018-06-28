

def fib(number):
    if number == 1 or number == 2:
        return 1
    else:
        return fib(number - 1) + fib(number - 2)


number = int(input())

print(fib(number))
