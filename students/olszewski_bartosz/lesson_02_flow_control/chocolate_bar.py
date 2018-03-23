dimension_a = int(input())
dimension_b = int(input())
squares = int(input())
if (dimension_a * dimension_b) > squares:
    if (squares % dimension_a == 0) or (squares % dimension_b == 0):
        print('YES')
    else:
        print('NO')
else:
    print('NO')
