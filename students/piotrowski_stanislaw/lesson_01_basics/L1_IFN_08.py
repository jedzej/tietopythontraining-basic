#https://snakify.org/lessons/integer_float_numbers/problems/total_cost/
#piotrsta

a = int(input('Cena babeczki - "czesc dolarowa": '))
b = int(input('Cena babeczki - "czesc centowa": '))
n = int(input('Ile babeczek?: '))

total_cents = n * (a * 100 + b)
dollars = total_cents // 100
cents = total_cents % 100
print('Calkowity koszt wynosi (dollary, centy): ')
print(dollars, cents)
