def capitalize(words):
    cap_words = []
    for word in words:
        capitalized = word[0].upper() + word[1:]
        cap_words.append(capitalized)
    return cap_words


if __name__ == '__main__':
    words = [s for s in input().split()]
    print(" ".join(capitalize(words)))
