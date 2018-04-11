def sumdigits(a):
    b = 0

    while a:
        b += a % 10
        a //= 10
    return b


a = int(input("Number: "))
print("The sum is: " + str(sumdigits(a)))
