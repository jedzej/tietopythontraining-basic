DIST_BETWEEN_SMALL_AND_BIG_LETTER = 32


def capitalize_word(word):
    uppercase_array=[]
    for i in range(len(word)):
        if(ord(word[i][0])) > 95:
            uppercase_word = \
                ''.join(chr(ord(word[i][0]) -
                            DIST_BETWEEN_SMALL_AND_BIG_LETTER) + word[i][1:])
            uppercase_array.append(uppercase_word)
        else:
            uppercase_array.append(word[i])
    return uppercase_array


def uppercase(word):
    new_word = word.split()
    big_words = capitalize_word(new_word)
    finish_string = ''
    for i in range(len(big_words)):
        finish_string = ' '.join(str(i) for i in big_words)
    return(finish_string)


def main():
    user_word = str(input())
    print(uppercase(user_word))


if __name__ == '__main__':
    main()
