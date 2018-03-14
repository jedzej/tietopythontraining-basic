#https://snakify.org/lessons/integer_float_numbers/problems/digital_clock/
#piotrsta

print('Podaj liczbe minut od polnocy: ')
num_of_minutes = int(input())

hours = num_of_minutes // 60
minutes = num_of_minutes % 60
print('Godzina minut: ')
print(hours, minutes)
