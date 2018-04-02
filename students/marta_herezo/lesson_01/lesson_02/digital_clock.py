print('Give minutes: ')
N = int(input())

h = N // 60
second = N % 60

print('Now is: ' + str(h) + ':' + str(second))
