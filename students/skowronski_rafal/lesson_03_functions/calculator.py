# Refactored version of 'Calculator' project


def _execute(function):
    operand_1 = int(input('Input 1st operand: '))
    operand_2 = int(input('Input 2nd operand: '))

    return function(operand_1, operand_2)


def _help():
    print('\nWelcome to the machine:')
    print('a - add')
    print('s - subtract')
    print('m - multiply')
    print('d - divide')
    print('p - power')
    print('h,? - help')
    print('q - QUIT')


def _exit():
    print('GOOD BYE')
    exit(0)


def _main():

    functions = {
        'a': lambda: _execute(lambda x, y: x + y),
        's': lambda: _execute(lambda x, y: x - y),
        'm': lambda: _execute(lambda x, y: x * y),
        'd': lambda: _execute(lambda x, y: x / y),
        'p': lambda: _execute(lambda x, y: x ** y),
        'h': lambda: _help(),
        '?': lambda: _help(),
        'q': lambda: _exit()
    }

    _help()

    while True:
        option = input('\nEnter option: ')
        print(functions[option]())


if __name__ == '__main__':
    _main()
