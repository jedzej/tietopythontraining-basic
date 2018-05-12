def cubes():
    n, m = [int(s) for s in input().split()]
    n_elements = {int(input()) for s in range(n)}
    m_elements = {int(input()) for s in range(m)}

    intersection = n_elements & m_elements
    to_n_belong = n_elements ^ intersection
    to_m_belong = m_elements ^ intersection

    for s in intersection, to_n_belong, to_m_belong:
        print(len(s))
        if len(s) > 0:
            for i in range(len(s)):
                print(s.pop())
        else:
            print()


cubes()
