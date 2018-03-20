

def collatz_calculation(value):
    try:
        print(int(value))
    except ValueError:
        print('ValueError: invalid literal for int().')
        print('Please enter an integer!')
        return None
    if value == 1:
        return None
    elif value % 2 == 0:
        return collatz_calculation(value >> 1)
    elif value % 2 == 1:
        return collatz_calculation(3 * value + 1)


starting_value = input()

collatz_calculation(starting_value)
