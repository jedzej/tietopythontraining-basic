# https://automatetheboringstuff.com/chapter3/
# "The Collatz Sequence"
# piotrsta

def collatz(number):
    if int(number) % 2 == 0:
        value = int(number) // 2
        print(value)
    else:
        value = 3 * int(number) + 1
        print(value)
    return value

number = input()
while number != 1:
    number = collatz(number)








