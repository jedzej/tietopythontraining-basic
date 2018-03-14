from math import floor

number = float(input("Real number: "))
result = number - floor(number)
print("Fractional part: " + str(result))
