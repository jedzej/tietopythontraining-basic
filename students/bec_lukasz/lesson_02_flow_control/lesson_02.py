

def bishop_moves():

    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())

    if (abs(c - a)) == (abs(d - b)):
        print('YES')
    else:
        print('NO')


def queen_moves():

    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())

    if (abs(c - a)) == (abs(d - b)) or c == a or d == b:
        print('YES')
    else:
        print('NO')


def knight_move():

    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())

    if (c == a - 2) or (c == a + 2):
        if (d == b - 1) or (d == b + 1):
            print('YES')
        else:
            print('NO')

    elif (d == b - 2) or (d == b + 2):
        if (c == a - 1) or (c == a + 1):
            print('YES')
        else:
            print('NO')
    else:
        print('NO')


def chocolate_bar():

    n = int(input())
    m = int(input())
    k = int(input())

    if (k % n == 0 and k / n < m) or (k % m == 0 and k / m < n):
        print('YES')
    else:
        print('NO')


def leap_year():
    year = int(input())

    if year % 4 == 0 and year % 100 != 0:
        print('LEAP')
    elif year % 400 == 0:
        print('LEAP')
    else:
        print('COMMON')


def fractional():
    n = int(input())
    m = 1

    for i in range(1, n + 1):
        m *= i

    print(m)


def the_number_of_zeros():
    zeros = 0

    for i in range(int(input())):
        if int(input()) == 0:
            zeros += 1

    print(zeros)


def ladder():
    n = int(input())

    for i in range(1, n + 1):
        out = ''
        for j in range(1, i + 1):
            out += str(j)
        print(out)


def lost_card():
    n = int(input())
    card = 0
    for i in range(1, n + 1):
        card += i

    for i in range(n - 1):
        card -= int(input())

    print(card)


def the_second_maximum():
    greatest = 2
    second = 1
    element = int(input())
    while element != 0:
        if element > greatest:
            temporary = greatest
            greatest = element
            second = temporary
        elif second < element < greatest:
            second = element
        element = int(input())

    print(second)


# bishop_moves()
# queen_moves()
# knight_move()
# chocolate_bar()
# leap_year()
# fractional()
# the_number_of_zeros()
# ladder()
# lost_card()
# the_second_maximum()
