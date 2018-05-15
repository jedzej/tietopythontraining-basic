def sum_all(*args):
    result = 0
    for v in args:
        result += v
    return result


def main():
    print(sum_all(1, 2, 3, 4))


if __name__ == "__main__":
    main()
