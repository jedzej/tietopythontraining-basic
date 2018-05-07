

def swap_min_and_max(lst):
    if len(lst) < 2:
        return lst
    max_value = lst[0]
    min_value = lst[0]
    min_idx = 0
    max_idx = 0
    for i in range(len(lst)):
        if max_value < lst[i]:
            max_idx = i
            max_value = lst[i]
        elif min_value > lst[i]:
            min_idx = i
            min_value = lst[i]
    lst[min_idx], lst[max_idx] = lst[max_idx], lst[min_idx]


def main():
    lst = [int(x) for x in input().split()]
    swap_min_and_max(lst)
    print(lst)


if __name__ == '__main__':
    main()
