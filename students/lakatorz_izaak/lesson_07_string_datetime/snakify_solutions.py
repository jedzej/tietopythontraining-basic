def replace_the_substring():
    """Given a string. Replace in this string all the numbers 1 by the word
    one."""
    print(input().replace('1', 'one'))


def number_of_words():
    """ Given a string consisting of words separated by spaces. Determine
    how many words it has. To solve the problem, use the method count."""
    print(input().count(' ') + 1)


def swap_two_words():
    """Given a string consisting of exactly two words separated by a space.
    Print a new string with the first and second word positions swapped (the
    second word is printed first). """
    string_a, string_b = input().split(' ')
    print(string_b, string_a)


def main():
    replace_the_substring()
    number_of_words()
    swap_two_words()


if __name__ == "__main__":
    main()
