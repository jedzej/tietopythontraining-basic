a = int(input())
b = int(input())
c = int(input())
d = int(input())

knight_can_move = (
    (abs(a - c) == 2 and abs(b - d) == 1)
    or (abs(a - c) == 1 and 2 == abs(b - d))
)
if knight_can_move:
    print('YES')
else:
    print("NO")
