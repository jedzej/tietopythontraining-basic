def guess_the_number():
    set_of_rejected_numbers = set()
    try:
        n = int(input())
    except ValueError:
        print('You have to give a number try again')
        exit()

    set_of_possibility_result = set(range(1, n + 1))

    print(set_of_possibility_result)

    while True:
        shot = input("Enter integers separeted by space \n")

        if shot == 'HELP':
            break
        else:
            shot = set(int(s) for s in shot.split())

        answer = input('Please answer if secret number is in set of shots \n')
        if answer == 'YES':
            set_of_possibility_result &= shot
            print(
                'possibility number is in {}'.format(
                    set_of_possibility_result))
        if len(set_of_possibility_result) == 1:
            print(
                'You found my secret number {}'.format(
                    set_of_possibility_result))
            exit()
        if answer == 'NO':
            set_of_rejected_numbers |= shot

    result = set_of_possibility_result - set_of_rejected_numbers
    print(result)


def main():
    guess_the_number()


if __name__ == '__main__':
    main()
