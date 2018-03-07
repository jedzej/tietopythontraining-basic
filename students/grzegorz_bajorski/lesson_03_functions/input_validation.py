def collatz(number):
    if number % 2 == 0:
        return number // 2
    else:
        return 3 * number + 1

print('Enter number')
number = 0

while 1:
    try:
        number = int(input())
        if collatz(number) != 1:
            print(collatz(number))
        else:
            break
    except:
        print('enter an integer')

print('Got 1 - break')
