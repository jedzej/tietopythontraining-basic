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
if (abs(h1-h2) == 1 and abs(v1-v2) == 2 or
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
sum = 0
n = int(input())
for i in range(1, n+1):
    factorial *= i
    sum += factorial
print(sum)


# Ladder
n = int(input())
for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end='')
    print()


# Lost card
sum = 0
sum_all = 0
N = int(input())
for i in range(1, N):
    n = int(input())
    sum_all += i
    sum += n
print(sum_all + N - sum)


# The second maximum
max_a = 0
second_max = 0
while 1:
    a = int(input())
    if a == 0:
        break
    if a > max_a:
        second_max = max_a
        max_a = a
    else:
        if a > second_max:
            second_max = a
print(second_max)


# The number of elements equal to the maximum
max_a = 0
while 1:
    a = int(input())
    if a == 0:
        break
    if a > max_a:
        max_a = a
        number_of_elements = 0
    if a == max_a:
        number_of_elements += 1
print(number_of_elements)
