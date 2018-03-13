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

if y_delta == x_delta:
    print("YES")
else:
    #this may be H/V move, which is OK for queen
    if(y_delta == 0 or x_delta == 0):
        print("YES")
    else:    
        print("NO")
