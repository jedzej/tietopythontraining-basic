def bishop_moves():
    print('Determine whether a bishop can go from the first to the second in one move.')
    rownumberstart = int(input("Enter Row Number Start:"))
    columnnumberstart = int(input("Enter Column Number Start:"))
    rownumberend = int(input("Enter Row Number End:"))
    columnnumberend = int(input("Enter Column Number End: "))
    if abs(rownumberstart - rownumberend) == abs(columnnumberstart - columnnumberend):
        print('YES')
    else:
        print('NO')


def queen_move():
    print('Determine whether a queen can go from the first cell to the second in one move.')
    rownumberstart = int(input("Enter  row start number:"))
    columnnumberstart = int(input("Enter column Number Start:"))
    rownumberend = int(input("Enter row Number End:"))
    columnnumberend = int(input("Enter column Number End:"))
    if abs(rownumberstart - rownumberend) == abs(
            columnnumberstart - columnnumberend) or rownumberstart == rownumberend or Co == columnnumberend:
        print('YES')
    else:
        print('NO')


def knight_move():
    print('Determine whether a knight can go from the first cell to the second in one move')
    rownumberstart = int(input("Enter  row start number:"))
    columnnumberstart = int(input("Enter column Number Start:"))
    rownumberend = int(input("Enter row Number End:"))
    columnnumberend = int(input("fourth number:"))
    firstcell = abs(rownumberstart - rownumberend)
    secondcell = abs(columnnumberstart - columnnumberend)
    if firstcell == 1 and secondcell == 2 or firstcell == 2 and secondcell == 1:
        print('YES')
    else:
        print('NO')


def chocolate_bar():
    print('Determine whether it is possible to split Chocolate into specified squares')
    n = int(input("Enter chocolate bar width:"))
    m = int(input("Enter chocolate bar length:"))
    k = int(input("Enter planned chocolate squares:"))
    if k < n * m and ((k % n == 0) or (k % m == 0)):
        print('YES')
    else:
        print('NO')


def leap_year():
    print('Enter Year and check it is Leap Year or Not ')
    year = int(input())
    if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
        print('This is LEAP Year')
    else:
        print('This is COMMON Year')


def factorial():
    print("Enter integer and calculate n! value")
    res = 1
    n = int(input())
    for i in range(1, n + 1):
        res *= i
    print(res)


def adding_factorials():
    print("For given integer count sum ")
    a = int(input("Enter number: "))
    factorial = 1
    sum_of_factorials = 0
    for i in range(1, a + 1):
        factorial *= i
    sum_of_factorials += factorial
    print(sum_of_factorials)


def the_number_of_zeros():
    n = int(input("How many numbers? "))
    sum_of_zeros = 0
    for i in range(n):
        number = int(input("Type  number: "))
    if number == 0:
        sum_of_zeros += 1
    print(sum_of_zeros)


def ladder():
    n = int(input("How many steps?"))
    for k in range(1, n + 1):
        for l in range(1, k + 1):
            print(1, sep='', end='')
        print("")


def lost_card():
    n = int(input())
    sum_cards = 0
    for i in range(1, n + 1):
        sum_cards += i
    for i in range(n - 1):
        sum_cards -= int(input("Type card number: "))
    print(sum_cards)


def second_maximum():
    print("Enter positive integer and integer and end with 0")


first_max = int(input())
second_max = int(input())
if first_max < second_max:
    first_max, second_max = second_max, first_max
element = int(input())
while element != 0:
    if element > first_max:
        second_max, first_max = first_max, element
    elif element > second_max:
        second_max = element
    element = int(input())
print(second_max)


def the_number_of_elements_equal_to_the_maximum():
    first_max = 0
    max_num = 0
    element = -1
    while element != 0:
        element = int(input())
        if element > first_max:
            first_max, max_num = element, 1
        elif element == max:
            max_num = 1
    print(num_max)


if __name__ == '__main__':
# bishop_moves()
# queen_move()
# knight_move(
# chocolate_bar()
# leap_year()
# factorial()
# adding_factorials()
# the_number_of_zeros()
# ladder()
# lost_card()
# second_maximum()
# the_number_of_elements_equal_to_the_maximum()

pass
