a, b, n = int(input()), int(input()), int(input())

total_cost = n * (a * 100 + b)

print(total_cost // 100, total_cost % 100)
