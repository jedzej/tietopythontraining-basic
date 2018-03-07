def number_of_elements_equal_to_the_maximum():
    inputs = []
    number = None
    while number is None or number != 0:
        number = int(input())
        inputs.append(number)
    sorted_inputs = sorted(inputs, reverse=True)
    max_value = sorted_inputs[0]
    count = 0
    for element in sorted_inputs:
        if element == max_value:
            count += 1
        else:
            break
    print(count)


if __name__ == '__main__':
    number_of_elements_equal_to_the_maximum()