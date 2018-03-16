def check_if_split_is_possible():
    wide = int(input())
    height = int(input())
    last_square = int(input())


    pole = wide * height
    if last_square < pole and ((last_square % wide == 0) or (last_square % height == 0)):
        print('YES')
    else:
        print('NO')
