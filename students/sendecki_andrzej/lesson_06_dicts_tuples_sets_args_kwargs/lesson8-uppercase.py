def capitalize(lower_case_word):
    return word[0].upper() + word[1:]


my_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
words = my_text.split(" ")

capitalized_text = ''
capitalized_list = []

for word in words:
    capitalized_list.append(capitalize(word))

capitalized_text = ' '.join(capitalized_list)

print(my_text)
print(capitalized_text)
