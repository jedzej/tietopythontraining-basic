

def next_character(x):
    if x == '*':
        return '.'
    else:
        return '*'


def main():
    n, m = [int(x) for x in input().split()]
    row_start_character = '*'
    for i in range(n):
        row_start_character = next_character(row_start_character)
        character = row_start_character
        for j in range(m):
            print(character, end='')
            character = next_character(character)
        print()


if __name__ == '__main__':
    main()
