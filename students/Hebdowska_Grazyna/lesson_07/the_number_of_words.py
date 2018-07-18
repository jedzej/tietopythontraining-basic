def number_of_words():
    custom_text = input()
    number = custom_text.count(" ")
    if custom_text != '':
        print(number + 1)
    else:
        print(0)


number_of_words()
