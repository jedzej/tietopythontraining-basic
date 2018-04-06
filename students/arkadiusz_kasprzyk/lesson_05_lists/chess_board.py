def rep(x, length=None, times=None):
    if length is None:
        if times is None:
            raise ValueError
        else:
            x = x * times
    else:
        n = length // len(x) + ( length % len(x) > 0 )
        x = x * n
        x = x[:length]

    return x



def chess_board(m, n):
    chb = []
    for r in range(m):
        if r % 2:
            chb += [list(rep("*.",n))]
        else:
            chb += [list(rep(".*",n))]
    return chb


chb = chess_board(8,8)

for r in range(len(chb)):
    print("".join(chb[r]))


#for r in range(len(chb)):
#    for c in range(len(chb[r])):
#        print(chb[r][c], end='')
#    print("")
