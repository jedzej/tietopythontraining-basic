# The second maximum
lista = []
provide_input_data = True
while provide_input_data :
    a = int(input())
    lista.append(a)
    if a == 0:
        provide_input_data = False    
lista.sort()
print (lista[-2])


# The number of elements equal to the maximum
lista = []
provide_input_data = True
while provide_input_data :
    a = int(input())
    lista.append(a)
    if a == 0:
        provide_input_data = False
lista.sort()
print (lista.count(lista[-1]))

