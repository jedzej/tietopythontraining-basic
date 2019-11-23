how_many_secret_numbers = int(input("How many numbers you can think of? "))

allNumbers = set(range(1, how_many_secret_numbers + 1))
possibleNumbers = allNumbers

while True:
    guessNumber = input("Guess the numbers: ")
    if guessNumber == 'HELP':
        break
    guessNumber = {int(x) for x in guessNumber.split()}
    answer = input()
    if answer == 'YES':
        possibleNumbers &= guessNumber
    else:
        possibleNumbers &= allNumbers - guessNumber

print(' '.join([str(x) for x in sorted(possibleNumbers)]))
