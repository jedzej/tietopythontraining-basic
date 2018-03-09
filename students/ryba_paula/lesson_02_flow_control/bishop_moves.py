start_column, start_row, end_column, end_row = int(input()), int(input()), int(input()), int(input())

if abs(start_column - end_column) == abs(start_row - end_row):
    print ("YES")
else:
    print ("NO")