def main():
    print("Result:")
    value = int(input())
    series_of_numbers = set(range(1, value + 1))
    try_to_guess = input()
    while try_to_guess != "HELP":
        set_of_integers = set([int(i) for i in try_to_guess.split()])
        augustus_answer = input()
        if augustus_answer == "YES":
            series_of_numbers = series_of_numbers.intersection(set_of_integers)
        else:
            series_of_numbers = series_of_numbers.difference(set_of_integers)
        try_to_guess = input()
    for i in series_of_numbers:
        print(i, end=" ")


if __name__ == '__main__':
    main()
