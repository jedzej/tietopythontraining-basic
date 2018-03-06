def total_cost():
    dolars = int(input())
    cents = int(input())
    amount = int(input())
    wholePriceInCents = (dolars * 100 + cents ) * amount
    print(str(wholePriceInCents // 100) + ' ' + str(wholePriceInCents%100))


if __name__ == '__main__':
    total_cost()