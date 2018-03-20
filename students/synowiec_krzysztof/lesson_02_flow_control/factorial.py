def main():
    n = int(input())
    factorial = 1
    for x in range(2, n+1):
        factorial *= x
    print(factorial)

if __name__ == '__main__':
    main()
