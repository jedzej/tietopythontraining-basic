# Function capitalize(lower_case_word) that takes the lower case word
# and returns the word with the first letter capitalized


def capitalize(lower_case_word):
    lst = [word[0].upper() + word[1:] for word in lower_case_word.split()]
    lower_case_word = " ".join(lst)
    print(lower_case_word)
    return lower_case_word


text = str((input("Put string - use small letter: ")))
capitalize(text)

s = "ala's ma kota UK. kk"
capitalize(s)
