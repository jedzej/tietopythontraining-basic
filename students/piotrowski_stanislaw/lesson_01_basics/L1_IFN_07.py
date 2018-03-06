#https://snakify.org/lessons/integer_float_numbers/problems/digital_clock/
#piotrsta

print('Podaj liczbe minut od polnocy: ')
numOfMinutes = int(input())

hours=numOfMinutes//60
minutes=numOfMinutes%60
print('Godzina minut: ')
print(hours, minutes)


