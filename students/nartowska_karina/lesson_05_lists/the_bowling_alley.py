def the_bowling_alley(number_of_pins, action_list):
    state = []
    for i in range(number_of_pins):
        state.append("I")
    for i in action_list:
        for j in range(i[0], i[1] + 1):
            state[j - 1] = '.'
    booling_allay_image = ''.join(state)
    print("Result:")
    return booling_allay_image


def pin_input(number_of_balls):
    result = []
    for i in range(number_of_balls):
        result.append(data())
    return result


def data():
    input_value = input().split()
    output_value = []
    for j in input_value:
        output_value.append(int(j))
    return output_value


def main():
    print("Enter a list value:")
    list_value = data()
    number_of_pins = list_value[0]
    number_of_balls = list_value[1]
    print(the_bowling_alley(number_of_pins, pin_input(number_of_balls)))


if __name__ == "__main__":
    main()
