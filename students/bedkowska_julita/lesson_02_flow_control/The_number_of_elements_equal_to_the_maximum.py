maximum = 0
result = 0
i = int(input())
while i != 0:
    if i > maximum:
        maximum = i
        result = 0
    if i == maximum:
        result += 1
    i = int(input())

print('{} {}'.format('The number of elements equal to the maximum', result))
