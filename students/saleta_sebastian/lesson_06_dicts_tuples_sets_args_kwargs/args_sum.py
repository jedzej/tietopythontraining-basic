def sum_all(*args):
    summary = 0
    for arg in args:
        summary += arg
    print(summary)


def main():
    sum_all(1,2,3,4,5,6)


if __name__ == '__main__':
    main()
