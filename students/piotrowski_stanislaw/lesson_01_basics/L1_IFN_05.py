#https://snakify.org/lessons/integer_float_numbers/problems/digit_after_decimal_point/
#piotrsta

print('Podaj dodatnia liczbe rzeczywista: ')
num = float(input())

frac2 = int(num * 10) % 10
print('Pierwsza cyfra czesci dziesietnej tej liczby wynosi: ' + str(frac2))
