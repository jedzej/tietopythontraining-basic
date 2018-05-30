# uppercase.py


def capitalize_word(word):
    """
    Parameters
    ----------
    word: str

    Returns
    -------
    word_cap: str
        First letter of `word` turned to uppercase (if it's a letter).

    Examples
    --------
    capitalize_word("spam")         # 'Spam'
    capitalize_word("Spam")         # 'Spam'
    capitalize_word("_spam")        # '_spam'
    capitalize_word(" spam")        # ' spam'
    capitalize_word("_spam eggs")   # '_spam eggs'
    """
    if len(word) > 0:
        word0 = word[0]
        char0 = ord(word0)
        if char0 in range(97, 123):
            word0 = chr(char0 - 32)

        word_cap = word0 + word[1:]
    else:
        word_cap = ""
    return word_cap


def capitalize(text):
    """
    Parameters
    ----------
    text: str

    Returns
    -------
    text_cap: str
        Each word of `txt` capitalized.

    Examples
    --------
    capitalize("spam and eggs")     # 'Spam And Eggs'
    capitalize(" spam and eggs")    # ' Spam And Eggs'
    capitalize("spam and eggs ")    # 'Spam And Eggs '
    capitalize("?sPam aNd eegGs ")  # '?sPam ANd EgGs '
    capitalize("  spam  .eGgs . ")  # '  Spam  .eGgs . '
    capitalize(" spam   .eGgs    spam      eggS ")  # ' Spam   .eGgs    Spam      EggS '
    """
    words = text.split(" ")
    words = list(map(capitalize_word, words))
    return " ".join(words)
    #return words

if __name__ == "__main__":

    txt = input("input text: ")
    print()
    print(capitalize(txt))


"""
Notes
-----

ord(" ")  ## 32

ord("A")  ## 65
ord("Z")  ## 90

for k in range(90, 98):
    print("{} : {}".format(k, chr(k)))

chr(91)

ord("a")  ## 97
ord("z")  ## 122

ord("z") - ord("Z")  ## 32
"""
