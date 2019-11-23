list_to_fill = []


def reverse_order():
    print('Type number')
    while True:
        number = int(input())
        list_to_fill.append(number)
        if number == 0:
            for x in list_to_fill[::-1]:
                print(x)
            break

reverse_order()
