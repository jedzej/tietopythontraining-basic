def bowling(N, rolls):
    K = len(rolls)
    assert K > 0
    assert K <= N

    for l in rolls:
        assert len(l) == 2

    pins = list('I' * N)
    print(pins)

    for r in rolls:
        r[0] -= 1
        for k in range(*r):
            pins[k] = '.'

    return(pins)


print(bowling(5, [[1,2], [4,5]]))

ll = list(range(5))
ll[0:2] = [-1]*2