num = int(input("Input a three-digit number: "))


def sum(a, b, c):
    return a + b + c


result = sum(num % 1000 // 100, num % 100 // 10, num % 10)
print("Sum of digits: " + str(result))
