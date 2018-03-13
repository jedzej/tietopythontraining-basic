def main():
    n = int(input())
    factorial = 1
    sum = 0
    for x in range(1, n+1):
        factorial *= x
        sum += factorial
    print(sum)

if __name__ == '__main__':
    main()
