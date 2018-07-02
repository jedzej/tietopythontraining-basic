# swap_words.py


def swap_words(string):
    first, second = string.split(' ')
    return ' '.join([second, first])


""" old:
    k = string.find(" ")
    return string[(k + 1):] + " " + string[:k]
"""

if __name__ == "__main__":
    string = input("Give a string: ")
    print(swap_words(string))
