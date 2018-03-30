def zeros():
    numbers_count = int(input())
    count = 0
    while numbers_count != 0:
        number = int(input())
        if number == 0:
            count += 1
        numbers_count -= 1
    print(count)


if __name__ == '__main__':
    zeros()