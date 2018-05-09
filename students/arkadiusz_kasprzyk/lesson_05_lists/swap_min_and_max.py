def swap_min_max(numbers):
    """
    Parameters
    ----------
    numbers: int[]

    Returns
    -------
    numbers with maximum and minimum swapped.
    Only the first occurences of min and max are taken into account.

    Examples
    --------
    print(swap_min_max([3, 0, 1, 4, 7, 2, 6]))
    print(swap_min_max([3, 0, 0, 4, 7, 2, 6]))
    print(swap_min_max([3, 0, 1, 4, 7, 7, 6]))
    """
    if len(numbers) >= 2:
        lmin, lmax = min(numbers), max(numbers)
        imin, imax = numbers.index(lmin), numbers.index(lmax)
        numbers[imin], numbers[imax] = lmax, lmin
    return numbers
