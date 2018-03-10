from math import fabs

begin_row = int(input())
begin_col = int(input())
target_row = int(input())
target_col = int(input())

d_rows = begin_row - target_row
d_cols = begin_col - target_col

if fabs(d_rows) == fabs(d_cols) or d_rows == 0 or d_cols == 0:
    print("YES")
else:
    print("NO")
