n = int(input())

sum_card = 0
suma = 0

for i in range(1,n):
    sum_card += int(input())
    suma += i

print(suma+n - sum_card)

