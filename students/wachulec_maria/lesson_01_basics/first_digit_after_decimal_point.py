from math import floor

number = float(input("Real number: "))
result = number - floor(number)
print("First digit to the right of the decimal point is"
      ": " + str(result)[2])