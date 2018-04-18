# As first are defined functions.

def help():
    print('a - add')
    print('s - subtract')
    print('m - multiply')
    print('d - divide')
    print('p - power')
    print('h,? - help')
    print('q - QUIT')

    
def variables():
    var_1 = int(input('Enter a first variable \n'))
    var_2 = int(input('Enter a second variable \n'))
    return var_1, var_2


def add():
    var_1, var_2 = variables()
    print('Result of adding:')
    print(var_1 + var_2)

    
def sub():
    var_1, var_2 = variables()
    print('Result of subtract:')
    print(var_1 - var_2)

    
def multi():
    var_1, var_2 = variables()
    print('Result of multiply:')
    print(var_1 * var_2)

    
def divide():
    var_1, var_2 = variables()
    print('Result of dividing:')
    print(var_1 / var_2)

    
def power():
    var_1, var_2 = variables()
    print('Result of powering:')
    print(var_1 ** var_2)


# Program is defined as second
print('Choose one of the options below:')

help()

while True:
    print('Enter option:')

    option = input()

    if option == 'a':
        add()

    elif option == 's':
        sub()

    elif option == 'm':
        multi()

    elif option == 'd':
        divide()

    elif option == 'p':
        power()

    elif option == 'h':
        help()

    elif option == '?':
        help()

    elif option == 'q':
        print('GOOD BYE')
        break
