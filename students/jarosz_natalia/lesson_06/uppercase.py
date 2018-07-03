def capitalize(word):
    first_letter_small = word[0]
    first_letter_big = chr(ord(first_letter_small) - ord('a') + ord('A'))
    return first_letter_big + word[1:]


def main():
    source = input().split()
    res = []
    for word in source:
        res.append(capitalize(word))
    print(' '.join(res))


if __name__ == '__main__':
    main()
