def second_maximum():
    inputs = []
    number = None
    while number is None or number != 0:
        number = int(input())
        inputs.append(number)
    sorted_inputs = sorted(inputs, reverse=True)
    max_value = sorted_inputs[0]
    for element in sorted_inputs:
        if element == max_value:
            continue
        else:
            print(element)
            break


if __name__ == '__main__':
    second_maximum()