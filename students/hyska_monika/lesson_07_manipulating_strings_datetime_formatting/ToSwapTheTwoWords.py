# Given a string consisting of exactly two words separated by a space.
# Print a new string with the first and second word positions swapped
# (the second word is printed first).


# function cut string to half and display swapped
def change_string(text):
    half = int((len(text) / 2) + (len(text) % 2 > 0))
    second_part = text[half:]
    first_part = text[:half]
    print(second_part + first_part)


# correct function for this task
def swap_2_words(text):
    word1, word2 = text.split(' ')
    changed_text = word2 + ' ' + word1
    print(changed_text)


my_string = 'Ani Aladddddddd'
my_string2 = 'Ani5 Ala'
my_string3 = 'A sdfdfdsfsd'

swap_2_words(my_string)
swap_2_words(my_string2)
swap_2_words(my_string3)

# -----------------
print('')
my_string = 'AniAla'
my_string2 = 'Ani5Ala'
my_string3 = 'A'

change_string(my_string)
change_string(my_string2)
change_string(my_string3)
