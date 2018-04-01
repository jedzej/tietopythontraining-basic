a = int(input())
b = int(input())
c = int(input())

min1 = a//2 + a%2
min2 = b//2 + b%2
min3 = c//2 + c%2

print('min number of desks: ' + str(min1 + min2 + min3))