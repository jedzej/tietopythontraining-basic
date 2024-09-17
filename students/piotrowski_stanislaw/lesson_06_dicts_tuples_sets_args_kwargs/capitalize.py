# https://snakify.org/lessons/functions/problems/capitalize/
# Uppercase
# piotrsta


def capitalize(lower_case_word):
    first_uppercase_letter_word = []
    split_list = lower_case_word.split()
    for elem in split_list:
        new_elem = chr(ord(elem[0]) - 32) + elem[1:]
        first_uppercase_letter_word.append(new_elem)

    return print(" ".join(str(elem) for elem in first_uppercase_letter_word))


if __name__ == "__main__":
    input_string = 'harry potter'
    capitalize(input_string)
