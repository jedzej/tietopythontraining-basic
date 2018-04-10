def bowling(N, rolls):

    if N < 0:

        raise ValueError

    elif N == 0:

        pins = []

    else:

        for r in rolls:
            if len(r) != 2: raise ValueError

        pins = list('I' * N)

        for r in rolls:
            r[0] -= 1
            for k in range(*r):
                pins[k] = '.'

    return(pins)


#print(bowling(5, [[1,2], [4,5]]))
#print(bowling(5, [[1,2], [4]]))
#print(bowling(5, []))
#print(bowling(0, [[1, 2]]))


