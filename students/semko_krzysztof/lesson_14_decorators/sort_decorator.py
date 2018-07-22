"""

Write @sort decorator that when applied to a function
that returns a list, sorts this list, so we can do this:

@sort
def data_feeder():
  return [4,2,1,3]

data_feeder() == [1,2,3,4] # <- this is True

"""


def sort(func):
    def sort_list():
        return sorted(func())
    return sort_list


@sort
def data_feeder():
    return [4, 2, 1, 3]


def main():
    print(data_feeder() == [1, 2, 3, 4])  # <- this is True


if __name__ == '__main__':
    main()
