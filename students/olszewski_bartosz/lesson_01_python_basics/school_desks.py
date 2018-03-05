print('Podaj liczebność klasy 1a')
a = int(input())
print('Podaj liczebność klasy 1b')
b = int(input())
print('Podaj liczebność klasy 1c')
c = int(input())

A_klasa = a//2+a%2
B_klasa = b//2+b%2
C_klasa = c//2+c%2

print ('liczba wymaganych ławek to:',A_klasa+B_klasa+C_klasa)