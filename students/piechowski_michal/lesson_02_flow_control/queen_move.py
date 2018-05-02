#!/usr/bin/env python3

column_start = int(input())
row_start = int(input())
column_end = int(input())
row_end = int(input())

column_diff = abs(column_start - column_end)
row_diff = abs(row_start - row_end)

if column_diff == row_diff or column_diff == 0 or row_diff == 0:
    print("YES")
else:
    print("NO")
