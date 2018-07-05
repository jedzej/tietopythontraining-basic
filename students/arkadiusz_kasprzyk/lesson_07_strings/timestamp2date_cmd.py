#! python
# timestamp2date.py

import sys
import datetime as dt


if len(sys.argv) < 2:
    print("Usage: python timestamp2date [unix_timestamp]")
    sys.exit()


def timestamp2date(ts):
    return dt.datetime.fromtimestamp(int(ts))


print("{:%Y-%m-%d %H:%M}".format(timestamp2date(sys.argv[1])))
