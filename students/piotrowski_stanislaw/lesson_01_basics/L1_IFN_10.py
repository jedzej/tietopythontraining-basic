#https://snakify.org/lessons/integer_float_numbers/problems/clock_face_2/
#piotrsta

#input - kat wskazowki godzinowej
angleHH = float(input('Podaj kat wskazowki godzinowej: '))

#kat wskazowski godzinowej w przeliczeniu na 1 minute
angleHH_1H = 360 / 12
angleHH_1M = angleHH_1H / 60
#kat wskazowski minutowej w przeliczeniu na 1 minute
angleMH_1M = 360 / 60

#obliczenie minut od polnocy
minsFromMidnight = angleHH / angleHH_1M
#print(mins)

#liczba minut po godzinie pelnej
minsFromFullHour = minsFromMidnight % 60
#obliczenia kata wskazowki minutowej
angleMM = minsFromFullHour * angleMH_1M

#input - kat wskazowki godzinowej
print(angleMM)
print('Jezeli kat wskazowki godzinowej wynosi ' + str(angleHH) + ', to kat wskazowki minutowej wynosi: ' + str(angleMM))
