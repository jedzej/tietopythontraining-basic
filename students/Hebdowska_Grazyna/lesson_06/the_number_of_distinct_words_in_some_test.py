def distings_words():
    all_strings = set()
    number_of_lines = int(input('How many lines of text: '))
    for i in range(number_of_lines):
        string = input(str(i + 1) + ' Line of text: ').split()
        all_strings.update(string)

    return len(all_strings)


print(distings_words())
