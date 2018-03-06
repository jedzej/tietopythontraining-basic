#https://snakify.org/lessons/integer_float_numbers/problems/tens_digit/
#piotrsta

print('Podaj liczbe calkowita: ')
num = int(input())

print('Liczba dziesiatek wynosi: ')
if len(str(num))<2:
    print('0')
else:
    print(str(num)[-2])



