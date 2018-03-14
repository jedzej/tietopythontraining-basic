#https://snakify.org/lessons/integer_float_numbers/problems/fractional_part/
#piotrsta

print('Podaj dodatnia liczbe rzeczywista: ')
num = float(input())

frac = num - int(num)
print('Czesc dziesietna tej liczby wynosi: ' + str(frac))
