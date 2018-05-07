# A sequence consists of integer numbers and ends with the number 0.
# Determine how many elements of this sequence are equal to its largest element.

lista = []
while True:
    a = int(input())
    if a != 0:
        lista.append(a)
    else:
        break

lista.sort()
max_elem = lista[-1]
print(lista.count(max_elem))