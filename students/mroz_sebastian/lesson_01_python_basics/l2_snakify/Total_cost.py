a = int(input())
b = int(input())
n = int(input())

total_cost = a * n + (b * n)
dollars = str(total_cost // 100)
cents = str(total_cost % 100)

print(dollars + " " + cents)
