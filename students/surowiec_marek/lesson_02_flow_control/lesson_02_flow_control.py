# Bishop moves
h1 = int(input())
v1 = int(input())
h2 = int(input())
v2 = int(input())
if (abs(h1-h2) == abs(v1-v2)):
    print('YES')
else:
    print('NO')


# Queen move
h1 = int(input())
v1 = int(input())
h2 = int(input())
v2 = int(input())
if (abs(h1-h2) == abs(v1-v2) or h1 == h2 or v1 == v2):
    print('YES')
else:
    print('NO')

# Knight move
h1 = int(input())
v1 = int(input())
h2 = int(input())
v2 = int(input())
if (    abs(h1-h2) == 1 and abs(v1-v2) == 2 or
        abs(h1-h2) == 2 and abs(v1-v2) == 1):
    print('YES')
else:
    print('NO')


# Chocolate bar
n = int(input())
m = int(input())
k = int(input())
if (k % n == 0 and k/n < m) or (k % m == 0 and k/m < n):
    print('YES')
else:
    print('NO')

# Leap year
year = int(input())
if (year % 400 == 0 or year % 4 == 0 and year % 100 != 0):
    print('LEAP')
else:
    print('COMMON')


# Factorial
factorial = 1
n = int(input())
for i in range(1, n+1):
    factorial *= i
print(factorial)


# The number of zeros
zero_count = 0
N = int(input())
for i in range(N):
    n = int(input())
    if n == 0:
        zero_count += 1
print(zero_count)


# Adding factorials
factorial = 1
sum_of_factorials = 0
n = int(input())
for i in range(1, n+1):
    factorial *= i
    sum_of_factorials += factorial
print(sum_of_factorials)


# Ladder
n = int(input())
for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end='')
    print()


# Lost card
sum_of_cards = 0
sum_all = 0
N = int(input())
for i in range(1, N):
    n = int(input())
    sum_all += i
    sum_of_cards += n
print(sum_all + N - sum_of_cards)


# The second maximum
maximum = 0
second_maximum = 0
while True:
    a = int(input())
    if a == 0:
        break
    if a > maximum:
        second_maximum = maximum
        maximum = a
    else:
        if a > second_maximum:
            second_maximum = a
print(second_maximum)


# The number of elements equal to the maximum
maximum = 0
while True:
    a = int(input())
    if a == 0:
        break
    if a > maximum:
        maximum = a
        number_of_elements = 0
    if a == maximum:
        number_of_elements += 1
print(number_of_elements)
