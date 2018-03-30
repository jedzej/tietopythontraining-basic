start_column = int(input("Start column: "))
start_row = int(input("Start row: "))
end_column = int(input("End column: "))
end_row = int(input("End row: "))


delta_columns = abs(start_column - end_column)
delta_rows = abs(start_row - end_row)
if delta_columns == delta_rows:
    print("YES")
else:
    print("NO")
