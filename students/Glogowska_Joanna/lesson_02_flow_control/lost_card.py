print('Number of cards in a set: ')
cards = int(input())
print('Enter ' + str(cards - 1) + ' numbers between 1 and ' +
      str(cards) + ': ')
insum = 0
tehsum = 0
for j in range(cards + 1):
    tehsum += j
for i in range(cards - 1):
    print('Card number ' + str(i + 1) + ': ')
    insum += int(input())
print('The lost card is: ')
print(tehsum - insum)
