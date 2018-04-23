# uppercase.py


def capitalize_0(word):
    """
    Parameters
    ----------
    eord: str

    Returns
    -------
    word_cap: str
        First letter of `word` turned to uppercase (if it's a letter).

    Examples
    --------
    capitalize_0("aqq")
    capitalize_0("Aqq")
    capitalize_0("_qq")
    capitalize_0("_qq ryq")
    """
    word0 = word[0]
    char0 = ord(word0)
    if char0 in range(97, 123):
        word0 = chr(char0 - 32)
    word = word0 + word[1:]
    return word


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
    capitalize("ab cd efg")
    capitalize(" ab cd efg")
    capitalize("ab cd efg ")
    capitalize("?ab cD _efg ")
    capitalize("  ab  .cD . ")
    """
    text_cap = ""
    a = 0
    n = len(text)
    while a < n:
        step = text[a:].find(" ") + 1
        if step:
            b = a + step
            text_cap += capitalize_0(text[a:b])
            a = b
        else:
            text_cap += capitalize_0(text[a:])
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
