def sum_all(*args):
    summary = 0
    for argument in args:
        summary += argument
    return summary


def main():
    print(sum_all(2, 4, 6, 12))


if __name__ == "__main__":
    main()
