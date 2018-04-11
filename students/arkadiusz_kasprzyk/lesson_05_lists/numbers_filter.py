def numbers_filter(numbers, range):
    """
    Filtering out values in range from numbers.

    Parameters
    ----------
    numbers: str[] with numbers
    range: range(n), n: int

    Returns
    -------
    numbers without elements in range

    Examples
    --------
    numbers_filter(['2', '0', '8', '3'], range(3))
    numbers_filter(['-1', '2', '0', '8', '3'], range(3))
    """
    return [int(s) for s in numbers if int(s) not in range]
