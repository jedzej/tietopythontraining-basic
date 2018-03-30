def str_to_list_of_int(string):
    numbers = string.split()
    list_of_number = []
    for value in numbers:
        list_of_number.append(int(value))
    return list_of_number


def up_poits_line(number_of_pins):
    pins = ''
    for pins in range(0, number_of_pins):
        pins.__add__('I')
    return pins


def shooting_points(poits_line = str, start_point, stop_poits):
    start_point = start_point - 1
    stop_poits = stop_poits - 1
    line_after_shot = []
    for i in range(0, len(poits_line)):
        line_after_shot.append(poits_line[i])
    poits_line = ''
    for poit_down in range(start_point - 1, stop_poits - 1):
        line_after_shot[poit_down] = '.'
        poits_line += line_after_shot
    return poits_line


def list_to_string(list_value):
    string = ''
    for value in list_value:
        string += str(value) + " "
    return string


def main():
    values = input()
    poits_line = up_poits_line(str_to_list_of_int(values)[0])
    number_of_players = str_to_list_of_int(values)[1]
    for player in range(0, number_of_players):
        shoot_from = str_to_list_of_int(input())[0]
        shoot_to = str_to_list_of_int(input())[1]
        shooting_points(poits_line, shoot_from, shoot_to)
    print(poits_line)


if __name__ == '__main__':
    main()
