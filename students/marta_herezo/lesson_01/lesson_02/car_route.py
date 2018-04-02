# N - kilometer/day
# M - distance in kilometer
print('Enter a distance of N kilometers per day = ')
N = int(input())

print('Enter a length of route = ')
M = int(input())

r = M % N

print(r)

Days = - (- M // N)

print('The number of days we need to cover the distance ' + str(M) + ' km is = ' + str(int(Days)))
