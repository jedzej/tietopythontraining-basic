def sum_all(*args):
    result = 0
    for arg in args:
        result = result + arg
    return result


def main():
    print(sum_all(3, 6, 9, 12))


if __name__ == "__main__":
    main()
