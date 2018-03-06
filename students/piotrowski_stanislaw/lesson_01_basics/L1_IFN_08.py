#https://snakify.org/lessons/integer_float_numbers/problems/total_cost/
#piotrsta

print('Cena babeczki - "czesc dolarowa": ')
A = int(input())    #dollars
print('Cena babeczki - "czesc centowa": ')
B = int(input())    #cents
print('Ile babeczek?: ')
N = int(input())

totalCents = N*(A*100 + B)
dollars = totalCents // 100
cents = totalCents % 100
print('Calkowity koszt wynosi (dollary, centy): ')
print(dollars, cents)

