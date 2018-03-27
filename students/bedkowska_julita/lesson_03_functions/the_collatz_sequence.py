def collatz(number):
    if number % 2 == 0:
        result = number // 2
        print(result)
        return result
    else:
        result = 3 * number + 1
        print(result)
        return result


num = int(input('Give the number: '))
while num != 1:
    num = collatz(num)
