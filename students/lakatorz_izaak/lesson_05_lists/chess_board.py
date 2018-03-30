# Given two numbers n and m. Create a two-dimensional array of size (n×m)
# and populate it with the characters "." and "*" in a checkerboard pattern.
# The top left corner should have the character "." .


def switch_sign(sign):
    if sign == '.':
        sign = '*'
    else:
        sign = '.'

    return sign


def main():
    rows_size, columns_size = (
        int(a) for a in input('Enter the rows and columns (m×n): ').split())

    start_sign = '.'
    for n in range(rows_size):
        current_sign = start_sign

        for m in range(columns_size):
            print(current_sign, end='')
            current_sign = switch_sign(current_sign)

        start_sign = switch_sign(start_sign)
        print('')


if __name__ == "__main__":
    main()
