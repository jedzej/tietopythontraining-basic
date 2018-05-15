def help():
    print('a - add')
    print('s - subtract')
    print('m - multiply')
    print('d - divide')
    print('p - power')
    print('h,? - help')
    print('q - QUIT')


def variables():
    add_var_1 = int(input('Input 1st operand: '))
    add_var_2 = int(input('Input 2nd operand: '))
    return add_var_1, add_var_2


def adding():
	add_var_1, add_var_2 = variables()
	print('Result:')
	print(add_var_1 + add_var_2)


def subtract():
	add_var_1, add_var_2 = variables()
	print('Result:')
	print(add_var_1 - add_var_2)


def multiply():
	add_var_1, add_var_2 = variables()
	print('Result:')
	print(add_var_1 * add_var_2)


def divide():
	add_var_1, add_var_2 = variables()
	print('Result:')
	print(add_var_1 / add_var_2)


def power():
	add_var_1, add_var_2 = variables()
	print('Result:')
	print(add_var_1 ** add_var_2)


print('Choose one of the options below:')

help()

while True:
	print('Enter option: ')

	option = input()

	if option == 'a':
		print("ADDING")
		adding()

	elif option == 's':
		print("SUBTRACT")
		subtract()

	elif option == 'm':
		print("MULTIPLY")
		multiply()

	elif option == 'd':
		print("DIVIDE")
		divide()

	elif option == 'p':
		print("POWER")
		power()

	elif option == 'h':
		print("HELP")
		help()

	elif option == '?':
		print("HELP")
		help()

	elif option == 'q':
		print('GOOD BYE')
		break
