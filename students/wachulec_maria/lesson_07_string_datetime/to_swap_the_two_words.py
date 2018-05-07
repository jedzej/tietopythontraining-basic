def swap_two_words():
    text = input()
    space_index = text.find(' ')
    return ' '.join((text[space_index + 1:], text[:space_index]))


r = swap_two_words()
print(r)
