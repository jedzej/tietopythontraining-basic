starting_parameters = input().split(' ')
pins_number = int(starting_parameters[0])
balls_number = int(starting_parameters[1])
pins_line = ['I'] * pins_number
for _ in range(balls_number):
    given_pair = input().split(' ')
    pins_line[int(given_pair[0]) - 1: int((given_pair[1]))] = \
        ['.'] * (int(given_pair[1]) - (int(given_pair[0])) + 1)
print(''.join(pins_line))
