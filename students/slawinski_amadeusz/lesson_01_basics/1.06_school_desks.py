# gets 3 numbers,
# divides them by 2 and adds rest of division to them
# and then sums them all up
a = int(input())
b = int(input())
c = int(input())

print ((a // 2 + a % 2) + (b // 2 + b % 2) + (c // 2 + c % 2))
