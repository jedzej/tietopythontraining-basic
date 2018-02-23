dollars, cents, cupcakes = int(input()), int(input()), int(input())

total_cost = cupcakes * (dollars * 100 + cents)

print(total_cost // 100, total_cost % 100)