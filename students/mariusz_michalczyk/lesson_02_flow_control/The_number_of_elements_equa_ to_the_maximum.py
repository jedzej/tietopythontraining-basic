counter = 0
maximum_nr = 0
entered_nr = -1
while entered_nr != 0:
    entered_nr = int(input())
    if entered_nr > maximum_nr:
        maximum_nr = entered_nr
        counter = 1
    elif entered_nr == maximum_nr:
        counter += 1
print(counter)
