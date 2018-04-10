array_size = input()
n = int((array_size.split(' '))[0])
m = int((array_size.split(' '))[1])
for x in range(n):
    chess_board = []
    for y in range(m):
        if (x + y) % 2 == 1:
            chess_board.append('*')
        else:
            chess_board.append('.')
    print(' '.join(chess_board))
