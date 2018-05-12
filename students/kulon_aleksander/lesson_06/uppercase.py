def func(a):
    b = []
    index = 0
    for char in a:
        if index == 0:
            b.append(chr(ord(a[index]) - 32))
        elif a[index - 1] == ' ':
            b.append(chr(ord(a[index]) - 32))
        else:
            b.append(a[index])
        index += 1
    return ''.join(b)


def main():
    a = 'hory pjoter'
    print(func(a))


if __name__ == '__main__':
    main()
