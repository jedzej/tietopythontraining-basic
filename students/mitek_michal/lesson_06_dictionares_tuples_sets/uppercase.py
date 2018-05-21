
def capitalize(lower_case_word):

    first_letter_capitalized_word = \
        lower_case_word[:1].upper() + lower_case_word[1:]
    return first_letter_capitalized_word


def capitalize_ascii():

    ascii_input = input().split()
    capitalized_ascii = []

    for i in ascii_input:
        capitalized_ascii.append(capitalize(i))

    print(' '.join(capitalized_ascii))


if __name__ == '__main__':
    capitalize_ascii()
