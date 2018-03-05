print ('Podaj liczbę minut')
a = int(input())
a = a%1440
godziny = a//60
minuty = a - godziny*60
print('Godzina wskazana na zegarze to',godziny,':',minuty)