begin_row = int(input())
begin_col = int(input())
target_row = int(input())
target_col = int(input())

d_rows = abs(begin_row - target_row)
d_cols = abs(begin_col - target_col)

if (d_cols == 2 and d_rows == 1) or (d_rows == 2 and d_cols == 1):
    print("YES")
else:
    print("NO")
