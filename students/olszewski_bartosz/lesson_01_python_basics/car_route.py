from math import ceil
print ('Podaj liczbę kilometrów do pokonania')
a = int(input())
print ('Podaj ile kilometrów samochód jest w stanie pokonać w ciągu dnia')
b = int(input())
x = a / b
y = ceil(x)
print('Samochód pokona zamierzony dystans w',y,'dni')