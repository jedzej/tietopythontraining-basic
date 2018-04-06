def bowling(N, rolls):
<<<<<<< HEAD
    """
    Parameters
    ----------
    N: int
        number of pins
    rolls: list of rolls
        roll: [a, b]
            a: int
            b: int
                a < b; pins from a to b are put down by this roll

    Returns
    -------
    List of all pins:
        if the pin is standing after all rolls being done then 'I' is in its place;
        if the pin is put down then '.' is in its place.

    Examples
    --------
    bowling(5, [[1, 2], [4, 5]])
    bowling(3, [])
    bowling(0, [[1, 2])

    """
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
=======
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
>>>>>>> 00 adziu/lesson_05_lists
