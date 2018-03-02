def number_of_elements_equal_to_the_maximum():
    inputs = []
    while True:
        number = int(input())
        if number == 0:
            break
        inputs.append(number)
    sorted_inputs = sorted(inputs, reverse=True)
    max = sorted_inputs[0]
    count = 0
    for element in sorted_inputs:
        if element == max:
            count += 1
        else:
            break
    print(count)


if __name__ == '__main__':
    number_of_elements_equal_to_the_maximum()