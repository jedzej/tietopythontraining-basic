<<<<<<< HEAD
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
        numbers[imin], numbers[imax]= lmax, lmin
    return numbers


=======
ll = [1, 4, 6, 3, 8, 6, 9, 0, 3, 5, 4, 6, 7, 4]

def swap_min_max(ll):
    lmin = min(ll)
    lmax = max(ll)
    imin = ll.index(lmin)
    imax = ll.index(lmax)
    ll[imin] = lmax
    ll[imax] = lmin
    return ll

print(swap_min_max(ll))
>>>>>>> 00 adziu/lesson_05_lists
