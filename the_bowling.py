n, k = (int(i) for i in input().split())
pairs = []

bowling_alley = ['I' for x in range(n)]

for i in range(k):
    x, y = (int(i) for i in input().split())
    for knock in range(x, y + 1):
        bowling_alley[knock - 1] = '.'

print(''.join(bowling_alley))