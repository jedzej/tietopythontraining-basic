# Input Validation
def collatz(number):
    if number % 2 == 0:
        return number // 2
    elif number % 2 == 1:
        return 3 * number + 1


while True:
    try:
        n = int(input())
        break
    except:
        print('Must be integer')

result = n

while result != 1:
    result = collatz(result)
    print(result)
