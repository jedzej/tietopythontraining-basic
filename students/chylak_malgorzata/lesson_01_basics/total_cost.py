dollars = int(input())
cents = int(input())
cupcakes = int(input())
cost = cupcakes * (100 * dollars + cents)
print(cost // 100, cost % 100)
