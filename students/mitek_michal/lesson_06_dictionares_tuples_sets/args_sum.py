
def sum_all(*args):

    result = 0

    for num in args:
        if not str(num).isdigit():
            return False
        else:
            result += int(num)
    return result


if __name__ == '__main__':
    sum_all()
