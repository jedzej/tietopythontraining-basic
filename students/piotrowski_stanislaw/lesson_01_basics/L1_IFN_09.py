#https://snakify.org/lessons/integer_float_numbers/problems/clock_face_1/
#piotrsta

print('Podaj liczbe godzin od polnocy: ')
H = int(input())
print('Podaj liczbe minut od pelnej godziny: ')
M = int(input())
print('Podaj liczbe sekund od pelnej minuty: ')
S = int(input())

angle1H = 360 / 12.
angle1M = angle1H / 60.
angle1S = angle1M / 60.

totalS = H * 3600 + M * 60 + S
#print(totalS)
angle = totalS * angle1S
print('Kat wskazowki godzinowej wynosi: ')
print(angle)

