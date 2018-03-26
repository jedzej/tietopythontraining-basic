def display_help():
    print("HELP")
    print("a - add")
    print("s - subtract")
    print("m - multiply")
    print("d - divide")
    print("p - power")
    print("h,? - help")
    print("q - QUIT")


def calculate(first_number, second_number, type_of_operation):
    if type_of_operation == 'a':
        return first_number + second_number

    elif type_of_operation == 's':
        return first_number - second_number

    elif type_of_operation == 'm':
        return first_number * second_number

    elif type_of_operation == 'd':
        return first_number / second_number

    elif type_of_operation == 'p':
        return first_number ** second_number
    else:
        print('Wrong type of operation')


while True:
    operation = input('Enter option(a, s, m, d, p, h, ?, q: ')
    if operation == 'h' or operation == '?':
        display_help()
    elif operation == 'q':
        print('EXIT')
        exit()
    else:
        first = float(input('First number: '))
        second = float(input('Second number: '))
        result = calculate(first, second, operation)
        if result is not None:
            print(result)
