#!/usr/bin/env python3


def main():
    set_of_rejected = set()
    answer = ''

    try:
        nums_range = int(input(
            "Please enter integer number of secret number's range\n"))
    except ValueError:
        print("Wrong number, try again\n")
        exit()

    possible_set = set(range(1, nums_range + 1))

    while True:
        input_message = input(
            "Enter integers separated with space in range of 1 to {}\n"
            "Or giveup with 'HELP' magic word\n".format(nums_range))

        if input_message == "HELP":
            break

        try:
            set_of_given_numbers = set(int(i) for i in input_message.split()
                                       if int(i) <= nums_range and int(i) > 0)
        except ValueError:
            print("You typed something wrong, try again\n")
            continue

        answer = input("Is there a secret number? [YES/NO]\n")
        if answer == "YES":
            possible_set &= set_of_given_numbers
            if len(possible_set) == 1:
                print("Gz! You have discovered secret number, it is: {}\n"
                      .format(*possible_set))
                exit()
        elif answer == "NO":
            set_of_rejected.update(set_of_given_numbers)
        else:
            print("Wrong input, this round won't be saved\n")

    print(*(possible_set - set_of_rejected))


if __name__ == "__main__":
    main()
