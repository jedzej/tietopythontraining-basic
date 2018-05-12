

# function for transforming list of strings into single comma-separated string
# the last item is separated from the rest with ' and ' string
def separate_with_commas(l):
    length = len(l)
    if length < 1:
        return ''
    elif length == 1:
        return l[0]
    else:
        result = ''
        for elem in range(length - 2):
            result += l[elem] + ', '
        result += l[length - 2] + ' and ' + l[length - 1]
    return result


def main():
    print(separate_with_commas(['apples', 'bananas', 'tofu', 'cats']))


if __name__ == '__main__':
    main()
