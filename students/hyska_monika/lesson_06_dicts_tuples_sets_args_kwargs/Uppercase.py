# Function capitalize(lower_case_word) that takes the lower case word
# and returns the word with the first letter capitalized


def capitalize(lower_case_word):
    lst = [word[0].upper() + word[1:] for word in lower_case_word.split()]
    capital_case_word = " ".join(lst)
    print(capital_case_word)
    return capital_case_word


text = str((input("Put string - use small letter: ")))
capitalize(text)

print("")
s = "ala's ma kota UK. kk"
capitalize(s)
