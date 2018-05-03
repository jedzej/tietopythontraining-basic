import re

word_to_check = input("Type the password you want to verify: ")

def check_password(word):
    high_letters = re.compile((r'[A-Z]'))
    check_if_high_letter_exists = high_letters.findall(word)
    if check_if_high_letter_exists:
        print("high letter CONFIRMED")
    else:
        print("No high letter")

def check_password_2(word):
    low_letter = re.compile((r'[a-z]'))
    check_if_low_letters_exist = low_letter.findall(word)
    if check_if_low_letters_exist:
        print("low letter CONFIRMED")
    else:
        print("No low letter")

def check_password_3(word):
    if len(word) >= 8:
        print("At least 8 charactes CONFIRMED")
    else:
        print("Not enough letters")

def check_password_4(word):
    number = re.compile((r'[0-9]'))
    check_if_number_exist = number.findall(word)
    if check_if_number_exist:
        print("A number CONFIRMED")
    else:
        print("No number")

check_password(word_to_check)
check_password_2(word_to_check)
check_password_3(word_to_check)
check_password_4(word_to_check)


'''

jedna cyfra
'''