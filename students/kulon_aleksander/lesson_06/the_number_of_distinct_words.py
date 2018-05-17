def count_words():
    a = int(input())

    text = ''
    result = {''}

    for i in range(a):
        text = text + '\n' + input()

    text = text.split()

    for i in text:
        result.add(i)

    print(len(result) - 1)


def main():
    count_words()


if __name__ == '__main__':
    main()
