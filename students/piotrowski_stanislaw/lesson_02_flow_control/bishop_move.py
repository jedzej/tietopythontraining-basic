# https://snakify.org/lessons/if_then_else_conditions/problems/bishop_move/
# piotrsta

col1 = int(input())
row1 = int(input())
col2 = int(input())
row2 = int(input())

if abs(col1 - col2) == abs(row1 - row2):
    print('YES')
else:
    print('NO')
