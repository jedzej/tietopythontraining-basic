A = int(input('Dollars = '))
B = int(input('Cents = '))
N = int(input('Number of cupcakes = '))

SUM_Cents = (A * 100 * N) + (B * N)

Cents = SUM_Cents % 100
Dollars = SUM_Cents // 100

print(Dollars, Cents)
