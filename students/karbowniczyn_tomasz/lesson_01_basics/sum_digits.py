#Sum of digits
#by tk

a = int(input())

setki= (a//100 % 100)
dziesiatki = (a//10 % 10)
jednosci = (a//1 % 10)

#print (setki)
#print (dziesiatki)
#print (jednosci)

suma = setki+dziesiatki+jednosci
print (suma)


