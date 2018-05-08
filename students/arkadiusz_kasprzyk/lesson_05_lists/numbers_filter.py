def numbers_filter(numbers, range):
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 03 on adziu/lesson_05_lists
    """
    Filtering out values in range from numbers.

    Parameters
    ----------
    numbers: str[] with numbers
    range: range(n), n: int
<<<<<<< HEAD

    Returns
    -------
    numbers without elements in range

    Examples
    --------
    numbers_filter(['2', '0', '8', '3'], range(3))
    numbers_filter(['-1', '2', '0', '8', '3'], range(3))
    """
    return [int(s) for s in numbers if int(s) not in range]
=======
    return [int(s) for s in numbers if int(s) not in range]

numbers = ['1', '2', '0', '8', '3']
range = range(3)
print(numbers_filter(numbers, range))
>>>>>>> 00 adziu/lesson_05_lists
=======

    Returns
    -------
    numbers without elements in range

    Examples
    --------
    numbers_filter(['2', '0', '8', '3'], range(3))
    numbers_filter(['-1', '2', '0', '8', '3'], range(3))
    """
    return [int(s) for s in numbers if int(s) not in range]
>>>>>>> 03 on adziu/lesson_05_lists
