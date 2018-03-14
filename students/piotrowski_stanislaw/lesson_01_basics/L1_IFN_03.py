#https://snakify.org/lessons/integer_float_numbers/problems/sum_of_digits/
#piotrsta

num = int(input('Podaj 3-cyfrowa liczbe calkowita: '))

units = num % 10
tens = num // 10 % 10
hundreds = num // 100

sum = (hundreds + tens + units)
print('Suma cyfr tej liczby wynosi: ' + str(sum))
