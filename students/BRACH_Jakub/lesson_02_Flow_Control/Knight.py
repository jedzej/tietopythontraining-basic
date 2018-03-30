x_base = int(input())
y_base = int(input())
x_move = int(input())
y_move = int(input())

x_delta = x_base - x_move
y_delta = y_base - y_move

if x_delta < 0:
    x_delta = x_delta * (-1)
if y_delta < 0:
    y_delta = y_delta * (-1)

if y_delta == 1 and x_delta == 2 or y_delta == 2 and x_delta == 1:
    print("YES")
else:
    print("NO")
