nowa_lista = [int(s) for s in input(
    "Enter a list of integer numbers separated by space: ").split()]

min_value = min(nowa_lista)
min_index = nowa_lista.index(min_value)
max_value = max(nowa_lista)
max_index = nowa_lista.index(max_value)

nowa_lista[min_index] = max_value
nowa_lista[max_index] = min_value

for elem in nowa_lista:
    print(elem, end=' ')
