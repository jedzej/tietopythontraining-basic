a = int(input())
b = int(input())
n = int(input())

dollars = n*a + (n*b) // 100
cents = (n*b) % 100

print(str(dollars) + ' ' + str(cents))
