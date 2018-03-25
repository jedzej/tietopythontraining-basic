

def input_validation_integer():
    while True:
        try:
            print('Set positive integer value')
            val = int(input())
            if val < 1:
                print('Error: Value is negative integer!')
            else:
                break
        except ValueError:
            print('ValueError: invalid literal for int().')
            print('Please enter an integer!')
    return val


def collatz_calculation(value):
    if value == 1:
        return 1
    elif value % 2 == 0:
        return value >> 1
    elif value % 2 == 1:
        return 3 * value + 1


collatz_value = input_validation_integer()

while True:
    collatz_value = collatz_calculation(collatz_value)
    print(str(collatz_value) + ', ', end='')
    if collatz_value == 1:
        break
