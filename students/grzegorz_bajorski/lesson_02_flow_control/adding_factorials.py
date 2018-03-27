n = int(input())
suma = 0
fractorial = 1

for i in range(1,n+1):
    fractorial *= i
    suma += fractorial

print(suma)

