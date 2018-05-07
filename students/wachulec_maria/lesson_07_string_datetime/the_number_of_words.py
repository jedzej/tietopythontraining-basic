def the_number_of_words():
    text = input()
    return text.count(' ') + 1


r = the_number_of_words()
print(r)
