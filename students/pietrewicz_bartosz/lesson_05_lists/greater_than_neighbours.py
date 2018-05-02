

def greater_than_neighbours(lst):
    result = 0
    for i in range(1, len(lst) - 1):
        if lst[i] > lst[i - 1] and lst[i] > lst[i + 1]:
            result += 1
    return result


def main():
    print(greater_than_neighbours([int(x) for x in input().split()]))


if __name__ == '__main__':
    main()
