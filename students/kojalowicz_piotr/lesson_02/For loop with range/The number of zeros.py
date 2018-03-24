noOfIntegers = int(input())
countOfZeros = 0
for number in range(noOfIntegers):
    integer = int(input())
    if integer == 0:
        countOfZeros += 1
print(countOfZeros)