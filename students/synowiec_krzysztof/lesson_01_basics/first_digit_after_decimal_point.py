def main():
    givenNumber = float(input())
    fractionalPart = givenNumber - int(givenNumber)
    firstDigit = int(fractionalPart * 10)
    print(firstDigit)

if __name__ == '__main__':
    main()
