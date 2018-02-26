
def main():
    givenNumber = int(input())
    lastDigit = givenNumber % 10
    tensDigit = givenNumber // 10 % 10
    hundredDigit = givenNumber // 100
    print (lastDigit + tensDigit + hundredDigit)

if __name__ == '__main__':
    main()