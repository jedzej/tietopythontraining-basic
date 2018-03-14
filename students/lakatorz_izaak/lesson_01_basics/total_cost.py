print("Enter dollars")
a = int(input())

print("Enter cents")
b = int(input())

print("Enter number of cupcakes")
n = int(input())


cents_value = b * n
dollars_value = a * n

cents_price = cents_value % 100
dollars_price = int(dollars_value + ((cents_value - cents_price) / 100))

print("Total cost:" + str(dollars_price) + " " + str(cents_price))
