def main():
    numberOfCards = int(input())
    sum = numberOfCards * (numberOfCards + 1) // 2
    for i in range(numberOfCards - 1):
        sum -= int(input())
    print(sum)

if __name__ == '__main__':
    main()