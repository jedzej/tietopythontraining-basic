def digital_clock():
    minutes = int(input())
    print(str(minutes // 60) + ' ' + str(minutes%60))


if __name__ == '__main__':
    digital_clock()