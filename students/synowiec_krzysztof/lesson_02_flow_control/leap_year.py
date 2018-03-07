def main():
    year = int(input())
    divisibleBy4 = year % 4 == 0
    notDivisibleBy100 = year % 100 != 0
    divisibleBy400 = year % 400 == 0

    if (divisibleBy4 and notDivisibleBy100) or divisibleBy400:
        print("LEAP")
    else:
        print("COMMON")

if __name__ == '__main__':
    main()

