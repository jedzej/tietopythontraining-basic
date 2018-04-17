def statement():
    first_number = int(input('Please write intiger number:\n'))
    second_number = int(input('Please Write another intiger number:\n'))
    if first_number > second_number:
        print('The smaller number is: ', second_number)
    elif first_number < second_number:
        print('The smaller number is: ', first_number)
    else:
        print('Both numbers are same', first_number, '', second_number)



def leap_year():
    year = int(input('Please write year:\n'))
    if year % 400 == 0:
        print('Leap')
    elif year % 4 == 0 and year % 100 != 0:
        print('Leap')
    else:
        print('Common')


def bishop_moves():
    start_col = int(input("Input start column number: "))
    start_row = int(input("Input start row number: "))
    end_col = int(input("Input end column number: "))
    end_row = int(input("Input end row number: "))

    d_col = abs(start_col - end_col)
    d_row = abs(start_row - end_row)

    if d_col == d_row:
        print("YES")
    else:
        print("NO")


def queen_move():
    start_col = int(input("Input start column number: "))
    start_row = int(input("Input start row number: "))
    end_col = int(input("Input end column number: "))
    end_row = int(input("Input end row number: "))

    d_col = abs(start_col - end_col)
    d_row = abs(start_row - end_row)

    if start_col == end_col or start_row == end_row or d_col == d_row:
        print("YES")
    else:
        print("NO")


def knight_move():
    start_col = int(input("Input start column number: "))
    start_row = int(input("Input start row number: "))
    end_col = int(input("Input end column number: "))
    end_row = int(input("Input end row number: "))

    d_col = abs(start_col - end_col)
    d_row = abs(start_row - end_row)

    if d_col == 2 and d_row == 1 or d_col == 1 and d_row == 2:
        print("YES")
    else:
        print("NO")


def factorial():
    n = int(input())

    factorial = 1

    for i in range(2, n + 1):
        factorial *= i

    print(factorial)



def the_number_of_zeros():
    result = 0

    for i in range(int(input())):
        if int(input()) == 0:
            result += 1

    print(result)


def add_factorials():
    n = int(input())

    factorial = 1
    result = 0

    for i in range(1, n + 1):
        factorial *= i
        result += factorial

    print(result)



def ladder():
    steps = int(input())
    row = ""

    if steps <= 9:
        for i in range(1, steps + 1):
            row += str(i)
            print(row, sep="")
    else:
        print("Number of steps must be max 9")



def lost_card():
    cards = int(input())

    sum_of_cards = 0

    for i in range(1, cards + 1):
        sum_of_cards += i

    for i in range(cards - 1):
        sum_of_cards -= int(input())

    print(sum_of_cards)


def the_second_maximum():
    largest = 0
    second_largest = 0

    while True:
        number = int(input())
        if number == 0:
            break
        if number > largest:
            second_largest, largest = largest, number
        elif number > second_largest and number < largest:
            second_largest = number

    print(second_largest)



def the_number_of_elements_equal_to_the_maximum():
    number = int(input())

    largest = 0
    largest_numbers = 0

    while number != 0:
        if number > largest:
            largest, largest_numbers = number, 1
        elif number == largest:
            largest_numbers += 1
        number = int(input())

    print(largest_numbers)









if __name__ == '__main__':
    # bishop_moves()
    # leap_year()
    # statement()
    # queen_move()
    # knight_move()
    # factorial()
    # the_number_of_zeros()
    # add_factorials()
    # ladder()
    # lost_card()
    # the_second_maximum()
    # the_number_of_elements_equal_to_the_maximum()
    pass
