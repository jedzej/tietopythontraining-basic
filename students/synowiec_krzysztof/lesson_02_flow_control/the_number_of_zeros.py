def main():
    n = int(input())
    numberOfzeros = 0
    for x in range(0, n):
        if (int(input()) == 0 ):
            numberOfzeros += 1
    print(numberOfzeros)

if __name__ == '__main__':
    main()
