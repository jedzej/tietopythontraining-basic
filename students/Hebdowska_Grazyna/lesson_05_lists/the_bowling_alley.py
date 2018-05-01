def data_input():
    data_in = input().split(" ")
    result = []
    for i in data_in:
        result.append(int(i))
    return result


def rolet_pin_input(b):
    result = []
    for i in range(b):
        result.append(data_input())
    return result


def booling(n, kik_list):
    allay = []
    for i in range(n):
        allay.append("I")

    for i in kik_list:
        for j in range(i[0], i[1] + 1):
            allay[j - 1] = '.'
    booling_allay = ''.join(allay)

    return booling_allay


numbers = data_input()
number_pins = numbers[0]
number_balls = numbers[1]
print(booling(number_pins, rolet_pin_input(number_balls)))
