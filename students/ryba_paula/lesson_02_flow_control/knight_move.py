start_column, start_row, end_column, end_row = int(input()), int(input()), int(input()), int(input())

if (abs(start_column - end_column) == 2 and abs(start_row - end_row) == 1) or (abs(start_column - end_column) == 1 and abs(start_row - end_row) == 2):
    print ("YES")
else:
    print ("NO")
