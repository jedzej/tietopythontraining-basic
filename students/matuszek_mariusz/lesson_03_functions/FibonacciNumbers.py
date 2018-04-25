def fib(a):
    if a >= 2:
        result = fib(a - 1) + fib(a - 2)
    else:
        result = a

    return result


while True:
    n = int(input('n = '))

    if n >= 0:
        break
    else:
        print("'n' should be non-negative integer !!")
        continue

print(fib(n))
