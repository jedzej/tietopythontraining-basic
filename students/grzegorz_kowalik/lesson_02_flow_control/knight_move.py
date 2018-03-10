from math import fabs

begin_row = int(input())
begin_col = int(input())
target_row = int(input())
target_col = int(input())

d_rows = begin_row - target_row
d_cols = begin_col - target_col

if (fabs(d_cols) == 2 and fabs(d_rows) == 1) or \
        (fabs(d_rows) == 2 and fabs(d_cols) == 1):
    print("YES")
else:
    print("NO")
