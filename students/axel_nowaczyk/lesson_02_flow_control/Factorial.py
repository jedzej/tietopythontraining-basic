def factorial():
    number = int(input())
    product = 1
    for i in range(2, number+1):
        product *= i
    print(product)


if __name__ == '__main__':
    factorial()