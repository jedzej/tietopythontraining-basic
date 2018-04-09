# Input Validation
while True:
    try:
        number = int(input("Enter the integer number "))
        break
    except ValueError:
        print ("Entered number is not integer")
        
def collatz(number):
    if number % 2 == 0:
        print (number // 2)
        return (number // 2)
    elif number % 2 == 1:
        print (3 * number +1)
        return (3 * number +1)
result = number
while result != 1:
    result = collatz(result)

