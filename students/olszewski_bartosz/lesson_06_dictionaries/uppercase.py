a = input()


def capitalize(sentence):
    for i in range(len(sentence)):
        if i == 0:
            b = ord(sentence[i]) - 32
            print(chr(b), end='')
        elif sentence[i - 1] == ' ':
            b = ord(sentence[i]) - 32
            print(chr(b), end='')
        else:
            print(sentence[i], end='')


capitalize(a)
