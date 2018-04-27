def main():
    number_range = int(input())
    main_set = set(range(1, number_range))

    while True:
        user_input = input()
        if user_input == 'HELP':
            print(main_set)
            break
        else:
            guessed_list = [int(n) for n in user_input.split()]
            opt = input('Contains?')
            if opt == 'YES':
                main_set &= set(guessed_list)
            elif opt == 'NO':
                main_set -= set(guessed_list)


if __name__ == "__main__":
    main()
