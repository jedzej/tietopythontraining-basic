# uppercase.py


<<<<<<< HEAD
def capitalize_word(word):
    """
    Parameters
    ----------
    word: str
=======
def capitalize_0(word):
    """
    Parameters
    ----------
    eord: str
>>>>>>> 20508ca4668bf458c74a7d554f4bab5ad0bf3736

    Returns
    -------
    word_cap: str
        First letter of `word` turned to uppercase (if it's a letter).

    Examples
    --------
<<<<<<< HEAD
    capitalize_word("spam")         # 'Spam'
    capitalize_word("Spam")         # 'Spam'
    capitalize_word("_spam")        # '_spam'
    capitalize_word(" spam")        # ' spam'
    capitalize_word("_spam eggs")   # '_spam eggs'
=======
    capitalize_0("aqq")
    capitalize_0("Aqq")
    capitalize_0("_qq")
    capitalize_0("_qq ryq")
>>>>>>> 20508ca4668bf458c74a7d554f4bab5ad0bf3736
    """
    word0 = word[0]
    char0 = ord(word0)
    if char0 in range(97, 123):
        word0 = chr(char0 - 32)
<<<<<<< HEAD
    word_cap = word0 + word[1:]
    return word_cap
=======
    word = word0 + word[1:]
    return word
>>>>>>> 20508ca4668bf458c74a7d554f4bab5ad0bf3736


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
<<<<<<< HEAD
    capitalize("spam and eggs")     # 'Spam And Eggs'
    capitalize(" spam and eggs")    # ' Spam And Eggs'
    capitalize("spam and eggs ")    # 'Spam And Eggs '
    capitalize("?sPam aNd egGs ")   # '?sPam ANd EgGs '
    capitalize("  spam  .eGgs . ")  # '  Spam  .eGgs . '
=======
    capitalize("ab cd efg")
    capitalize(" ab cd efg")
    capitalize("ab cd efg ")
    capitalize("?ab cD _efg ")
    capitalize("  ab  .cD . ")
>>>>>>> 20508ca4668bf458c74a7d554f4bab5ad0bf3736
    """
    text_cap = ""
    a = 0
    n = len(text)
    while a < n:
        step = text[a:].find(" ") + 1
        if step:
            b = a + step
<<<<<<< HEAD
            text_cap += capitalize_word(text[a:b])
            a = b
        else:
            text_cap += capitalize_word(text[a:])
=======
            text_cap += capitalize_0(text[a:b])
            a = b
        else:
            text_cap += capitalize_0(text[a:])
>>>>>>> 20508ca4668bf458c74a7d554f4bab5ad0bf3736
            break
    return text_cap


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
