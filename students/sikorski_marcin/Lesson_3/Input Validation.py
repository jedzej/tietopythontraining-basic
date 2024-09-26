def collatz(number):
    if number % 2 == 0:
        return number // 2
    elif number % 2 == 1:
        return 3 * number + 1
    else:
        print("What sort of input is this???")

while True:
    try:
        number_to_check = float(input("Enter a number for a collatz sequence: "))
        break
    except ValueError:
        print("This is not a number")

isThisNumberOne = collatz(number_to_check)

print(number_to_check)
print(is_this_number_one)
while is_this_number_one != 1:
    print(collatz(is_this_number_one))
    is_this_number_one = collatz(is_this_number_one)
