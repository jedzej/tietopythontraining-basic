def up_poits_line(number_of_pins):
    pins = ''
    for i in range(0, number_of_pins):
        pins += 'I'
    return pins


def shooting_points(poits_line = str, start_point = int, stop_poits = int):
    line_after_shot = []
    for i in range(0, len(poits_line)):
        line_after_shot.append(poits_line[i])
    for poit_down in range(start_point - 1, stop_poits):
        line_after_shot[poit_down] = '.'
    string = ''
    for t in line_after_shot:
        string += t
    return string


def main():
    values = input().split()
    poits_line = up_poits_line(int(values[0]))
    number_of_players = int(values[1])
    for player in range(0, number_of_players):
        values = input().split()
        start_point = int(values[0])
        stop_point = int(values[1])
        poits_line = shooting_points(poits_line, start_point, stop_point)
    print(poits_line)


if __name__ == '__main__':
    main()
