
def check_if_queen_can_move():

    initial_column = int(input("Provide initial column "))
    initial_row = int(input("Provide initial row "))

    final_column = int(input("Provide final column "))
    final_row = int(input("Provide final row "))

    if initial_column == final_column or initial_row == final_row\
            or initial_column - final_column == initial_row - final_row \
            or initial_column - final_column == final_row - initial_row:
        print('YES')
    else:
        print('NO')


check_if_queen_can_move()
