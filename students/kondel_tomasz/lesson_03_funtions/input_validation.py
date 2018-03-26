from the_collatz_sequence import *


def main():

    while True:
        input_string = input()
        try:
            input_int = int(input_string)
            calculated_value = collatz(input_int)
            if calculated_value == 1:
                break
        except ValueError:
            print('Please type int value')


if __name__ == '__main__':
    main()
