firstValue = int(input("Enter first value: "))
secondValue = int(input("Enter second value: "))
numberOfSquares = int(input("Enter number of squares: "))

if (numberOfSquares%firstValue== 0 and numberOfSquares/firstValue < secondValue) \
        or (numberOfSquares%secondValue== 0 and numberOfSquares/secondValue < firstValue):
    print("YES - we can divide choclate!")
else:
    print("NO - we can't divide chocolate")