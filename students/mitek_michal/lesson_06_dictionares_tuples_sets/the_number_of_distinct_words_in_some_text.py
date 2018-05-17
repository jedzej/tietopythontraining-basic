
def distinct_words():

    text = set()

    for _ in range(int(input())):
        text.update(input().split())

    text_len = len(text)
    print(text_len)


if __name__ == '__main__':
    distinct_words()
