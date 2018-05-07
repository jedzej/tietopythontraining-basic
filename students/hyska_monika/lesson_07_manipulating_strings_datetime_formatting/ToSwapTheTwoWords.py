# Given a string consisting of exactly two words separated by a space.
# Print a new string with the first and second word positions swapped
# (the second word is printed first).


def change_string(text):
    half = int((len(text) / 2) + (len(text) % 2 > 0))
    second_part = text[half:]
    first_part = text[:half]
    print(second_part + first_part)


my_string = 'AniAla'
my_string2 = 'Ani5Ala'
my_string3 = 'A'

change_string(my_string)
change_string(my_string2)
change_string(my_string3)
