#! python
# timestamp2date.py

import datetime as dt


def timestamp2date(ts):
    """
    Examples
    --------
    print("{:%Y-%m-%d %H:%M}".format(timestamp2date(0)))
    print("{:%Y-%m-%d %H:%M}".format(timestamp2date(88889)))
    print("{:%Y-%m-%d %H:%M}".format(timestamp2date(999999999)))
    """
    return dt.datetime.fromtimestamp(int(ts))


if __name__ == "__main__":
    tmstmp = input("Give timestamp (positive integer): ")
    print("{:%Y-%m-%d %H:%M}".format(timestamp2date(tmstmp)))
