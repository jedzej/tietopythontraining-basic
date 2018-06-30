def print_set(some_set):
    print(len(some_set))
    print(*[str(item) for item in sorted(some_set)])


def main():
    n, m = [int(s) for s in input().split()]
    a_colors, b_colors = set(), set()
    for i in range(n):
        a_colors.add(int(input()))
    for i in range(m):
        b_colors.add(int(input()))

    print_set(a_colors & b_colors)
    print_set(a_colors - b_colors)
    print_set(b_colors - a_colors)


if __name__ == '__main__':
    main()
