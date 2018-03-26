barlength = int(input('Height in cubes: '))
barwidth = int(input('Width in cubes: '))
n_squares = int(input('Is it possible to split it so that one of \
the parts will have exactly this number of squares: '))
if n_squares < barlength * barwidth and ((n_squares % barlength == 0) or
                                         (n_squares % barwidth == 0)):
    print('YES')
else:
    print('NO')
