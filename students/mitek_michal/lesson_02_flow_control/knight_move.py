
def check_if_knight_can_move():

    initial_column = int(input("Provide initial column "))
    initial_row = int(input("Provide initial row "))

    final_column = int(input("Provide final column "))
    final_row = int(input("Provide final row "))

    if abs(initial_column - final_column) == 2 and abs(initial_row - final_row) == 1 \
            or abs(initial_column - final_column) == 1 and abs(initial_row - final_row) == 2:
        print('YES')
    else:
        print('NO')


check_if_knight_can_move()
