def bishop_moves():
    print('Determine whether a bishop can go from the first to the second in one move.')
    RowNumberStart = int(input("Enter Row Number Start:"))
    ColumnNumberStart = int(input("Enter Column Number Start:"))
    RowNumberEnd = int(input("Enter Row Number End:"))
    ColumnNumberEnd = int(input("Enter Column Number End: "))
    if abs(RowNumberStart - RowNumberEnd) == abs(ColumnNumberStart - ColumnNumberEnd):
        print('YES')
    else:
        print('NO')


def Queen_move():
    print('Determine whether a queen can go from the first cell to the second in one move.')
    RowNumberStart = int(input("Enter  row start number:"))
    ColumnNumberStart = int(input("Enter column Number Start:"))
    RowNumberEnd = int(input("Enter row Number End:"))
    ColumnNumberEnd = int(input("Enter column Number End:"))
    if abs(RowNumberStart - RowNumberEnd) == abs(
            ColumnNumberStart - ColumnNumberEnd) or RowNumberStart == RowNumberEnd or Co == ColumnNumberEnd:
        print('YES')
    else:
        print('NO')


def Knight_move():
    print('Determine whether a knight can go from the first cell to the second in one move')
    RowNumberStart = int(input("Enter  row start number:"))
    ColumnNumberStart = int(input("Enter column Number Start:"))
    RowNumberEnd = int(input("Enter row Number End:"))
    ColumnNumberEnd = int(input("fourth number:"))
    FirstCell = abs(RowNumberStart - RowNumberEnd)
    SecondCell = abs(ColumnNumberStart - ColumnNumberEnd)
    if FirstCell == 1 and SecondCell == 2 or FirstCell == 2 and SecondCell == 1:
        print('YES')
    else:
        print('NO')


def Chocolate_bar():
    print('Determine whether it is possible to split Chocolate into specified squares')
    n = int(input("Enter chocolate bar width:"))
    m = int(input("Enter chocolate bar length:"))
    k = int(input("Enter planned chocolate squares:"))
    if k < n * m and ((k % n == 0) or (k % m == 0)):
        print('YES')
    else:
        print('NO')


def Leap_year():
    print('Enter Year and check it is Leap Year or Not ')
    year = int(input())
    if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
        print('This is LEAP Year')
    else:
        print('This is COMMON Year')


def Factorial():
    print("Enter integer and calculate n! value")
    res = 1
    n = int(input())
    for i in range(1, n + 1):
        res *= i
    print(res)


def Adding_factorials():
    print("For given integer count sum ")
    a = int(input("Enter number: "))
    factorial = 1
    sum_of_factorials = 0
    for i in range(1, a + 1):
        factorial *= i
    sum_of_factorials += factorial
    print(sum_of_factorials)


def The_number_of_zeros():
    n = int(input("How many numbers? "))
    sum_of_zeros = 0
    for i in range(n):
        number = int(input("Type  number: "))
    if number == 0:
        sum_of_zeros += 1
    print(sum_of_zeros)


def Ladder():
    n = int(input("How many steps?"))
    for k in range(1, n + 1):
        for l in range(1, k + 1):
            print(1, sep='', end='')
        print("")


def Lost_card():
    n = int(input())
    sum_cards = 0
    for i in range(1, n + 1):
        sum_cards += i
    for i in range(n - 1):
        sum_cards -= int(input("Type card number: "))
    print(sum_cards)


if __name__ == '__main__':
    # Bishop_moves()
    # Queen_move()
    # Knight_move()
    # Chocolate_bar()
    # Leap_year()
    # Factorial()
    # Adding_factorials()
    # The_number_of_zeros()
    Ladder()
# Lost_card()
# The_second_maximum
# The_number_of_elements_equal_to_the_maximum

pass
