
price_dollars = int(input('How many dollars: '))
price_cents = int(input('How many cents: '))
number_of_cupcakes = int(input('Number of cupcakes: '))

wallet_in_cents = (price_dollars * 100 + price_cents) * number_of_cupcakes

dollars = wallet_in_cents // 100
cents = wallet_in_cents - (dollars * 100)

print(dollars, cents)


