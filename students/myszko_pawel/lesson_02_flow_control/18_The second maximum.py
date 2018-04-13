# The sequence consists of distinct positive integer numbers and ends with the number 0.
# Determine the value of the second largest element in this sequence.
# It is guaranteed that the sequence has at least two elements.

lista = []
while True:
    a = int(input())
    if a !=0:
        lista.append(a)
    else:
        break

ciag = set(lista)
lista = list(ciag)
lista.sort()
print (lista[-2])
