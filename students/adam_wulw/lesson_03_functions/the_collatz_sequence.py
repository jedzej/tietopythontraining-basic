def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    else:
        print(3 * number + 1)
        return(3 * number + 1)


try:
    val = int(input('Enter number:\n'))
except ValueError:
    print('Error: Enterd numer is not a integer\n')
    exit()
while (True):
    val = collatz(val)
    if (val == 1):
        break
