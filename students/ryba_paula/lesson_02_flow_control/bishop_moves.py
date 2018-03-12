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
