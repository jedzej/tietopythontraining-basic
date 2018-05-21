def gtn(numbers):
    """
    Parameters
    ----------
    numbers: int[]

    Returns
    -------
    Number of elements of the `numbers` which are greater then its neighbours.
    First and last elements are not taken into account.

    Examples
    --------
    gtn([1, 4, 6, 3, 8, 6, 9, 0, 3, 5, 4, 6, 7, 4])
    """
    s = 0
    if len(numbers) >= 3:
        for k in range(1, len(numbers) - 1):
            if numbers[k] > numbers[k - 1] and numbers[k] > numbers[k + 1]:
                s += 1
    return s
