def lenght_segment():
    from math import sqrt
    def distance(x1, y1, x2, y2):
        return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    x1 = float(input("Enter x1:"))
    x2 = float(input("Enter x2:"))
    y1 = float(input("Enter y1:"))
    y2 = float(input("Enter y2:"))
    print(distance(x1, x2, y1, y2))


def negative_exponent():
    def power(a, n):
        result = 1.0
        if n > 0:
            for i in range(n):
                result *= a
        elif n == 0:
            result = 1.0
        else:
            for i in range(abs(n)):
                result *= 1 / a
                return result
            a = float(input("enter number:"))
            n = int(input("enter the exponent:"))
            print(power(a, n))


def exponentation(a, n):
    def power(a, n):
        if n >= 1:
            return a * power(a, n - 1)
        elif n == 0:
            return 1

    print(power(a, n))


def fib(n):
    if n == 1 or n == 2:
        return 1
    elif n == 0:
        return 0
    else:
        return fib(n - 1) + fib(n - 2)



if __name__ == '__main__':
    lenght_segment()
#negative_exponent()
#a = float(input("enter a number:"))
#n = int(input("enter the exponent:"))
#exponentation(a,n)
#print(exponentation(int(input()), int(input())))
#print(fib(int(input("enter number: "))))
# calculator.calculate()
# pass
