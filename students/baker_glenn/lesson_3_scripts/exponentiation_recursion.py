def exponentiation_recursion(num, exp, calculated_number):
    if exp > 1:
        exp -= 1
        calculated_number = calculated_number * num
        exponentiation_recursion(num, exp, calculated_number)
    else:
        print(str(calculated_number).rstrip('0').rstrip('.'))

while True:
    try:
        print("Please enter a real number")
        number = float(input())
        print("Please enter the exponent")
        exponent = int(input())
        break
    except:
        print("Please enter a real number first, followed by an integer")
counter = 0
exponentiation_recursion(number, exponent, number)
