print("Enter integer:")
a = int(input())

tens = int(((a % 100) - (a % 10)) / 10)

print("Tens digit: " + str(tens))