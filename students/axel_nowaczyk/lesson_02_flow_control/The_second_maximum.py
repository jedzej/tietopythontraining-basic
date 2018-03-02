def second_maximum():
    inputs = []
    while True:
        number = int(input())
        if number == 0:
            break
        inputs.append(number)
    sorted_inputs = sorted(inputs, reverse=True)
    max = sorted_inputs[0]
    for element in sorted_inputs:
        if element == max:
            continue
        else:
            print(element)
            break


if __name__ == '__main__':
    second_maximum()