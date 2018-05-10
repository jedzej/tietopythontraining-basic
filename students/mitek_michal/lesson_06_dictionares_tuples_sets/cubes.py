
def cubes():

    n_set, m_set = [int(s) for s in input().split()]
    n_set_colors, m_set_colors = set(), set()

    for i in range(n_set):
        n_set_colors.add(int(input()))

    for i in range(m_set):
        m_set_colors.add(int(input()))

    print_set(n_set_colors and m_set_colors)
    print_set(n_set_colors - m_set_colors)
    print_set(m_set_colors - n_set_colors)


def print_set(arg_set):

    sorted_set = sorted(arg_set)

    print(len(arg_set))
    print(*[str(item) for item in sorted_set])


if __name__ == '__main__':
    cubes()
