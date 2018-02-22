a = int(input())
b = int(input())
n = int(input())

total_cost = n * (a * 100 + b)

print(total_cost // 100, total_cost % 100)