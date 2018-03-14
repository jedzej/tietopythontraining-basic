#https://snakify.org/lessons/integer_float_numbers/problems/clock_face_1/
#piotrsta1

H = int(input('Podaj liczbe godzin od polnocy: '))
M = int(input('Podaj liczbe minut od pelnej godziny: '))
S = int(input('Podaj liczbe sekund od pelnej minuty: '))

angle1H = 360 / 12.
angle1M = angle1H / 60.
angle1S = angle1M / 60.

totalS = H * 3600 + M * 60 + S
angle = totalS * angle1S
print('Kat wskazowki godzinowej wynosi: ')
print(angle)
