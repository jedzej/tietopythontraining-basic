a = int(input())
b = int(input())

if a < b:
    a, b = b, a
sequence_element = b

while sequence_element != 0:
    sequence_element = int(input())
    if sequence_element > a:
        b = a
        a = sequence_element
    if a > sequence_element > b:
        b = sequence_element
else:
    print(b)
