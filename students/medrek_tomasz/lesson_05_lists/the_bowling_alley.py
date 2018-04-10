#!/usr/bin/env python3


def the_bowling_alley(array):
    pins = array[0][0]
    rolls = array[0][1]
    output_list = ['I'] * pins

    for row_no in range(1, rolls + 1):
        for i in range(array[row_no][0] - 1, array[row_no][1]):
            output_list[i] = '.'

    return output_list


def main():
    try:
        first_row = [int(i) for i in input(
            "Please enter two integers separated with space\n").split()]
        rolls = first_row[1]
        user_array = []
        user_array.append(first_row)
        for i in range(rolls):
            single_row = [int(i) for i in input(
                "Please enter two numbers separated with space\n").split()]
            user_array.append(single_row)
    except IndexError:
        print("Try again: two numbers separated with space, then hit enter")
        exit()
    except ValueError:
        print("Try again using integer numbers only, thanks")
        exit()

    print(''.join(str(i) for i in the_bowling_alley(user_array)))


if __name__ == "__main__":
    main()
