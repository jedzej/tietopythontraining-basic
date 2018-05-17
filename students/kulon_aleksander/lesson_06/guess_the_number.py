def guess():
    n = int(input())
    possible = []
    not_possible = []
    numbers = []
    beatrice_says = ''

    while beatrice_says != 'HELP':
        beatrice_says = str(input())
        if beatrice_says == 'YES':
            for i in range(n + 1):
                if i not in numbers and i not in not_possible:
                    not_possible.append(i)
                else:
                    if i not in possible:
                        possible.append(i)
        elif beatrice_says == 'NO':
            for i in numbers:
                if i not in not_possible:
                    not_possible.append(i)
        elif beatrice_says != 'HELP':
            numbers = []
            for i in beatrice_says.split():
                numbers.append(int(i))

    for i in not_possible:
        if i in possible:
            possible.remove(i)
    test = [str(i) for i in possible]
    print(' '.join(test))


def main():
    guess()


if __name__ == '__main__':
    main()
