integer_list = []

input_int = int(input())

while input_int != 0:
    integer_list.append(input_int)
    input_int = int(input())

integer_list.sort()
print(integer_list[len(integer_list) - 2])
