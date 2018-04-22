def swamp_two_words(words):
    space = words.find(" ")
    print(words[space + 1:], words[:space])


words = input()
swamp_two_words(words)
