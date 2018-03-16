def check_if_split_is_possible():
    wide = int(input())
    height = int(input())
    square = int(input())
    field = wide * height

    if square < field and ((square % wide == 0) or (square % height == 0)):
        print('YES')
    else:
        print('NO')


if __name__ == '__main__':
    check_if_split_is_possible()
