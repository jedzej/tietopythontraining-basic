start_column, start_row, end_column, end_row = int(input()), int(input()), int(input()), int(input())

if start_column == end_column or start_row == end_row or abs(start_column - end_column) == abs(start_row - end_row):
    print ("YES")
else:
    print ("NO")
