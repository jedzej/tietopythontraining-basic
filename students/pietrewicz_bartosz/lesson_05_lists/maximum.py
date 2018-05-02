

def main():
    rows, columns = [int(x) for x in input().split()]
    max_value = 0
    max_row = -1
    max_column = 0
    for i in range(rows):
        row = [int(x) for x in input().split()]
        # initialize maximal values from first element
        if max_row == -1:
            max_row = 0
            max_value = row[0]
        for j in range(columns):
            if row[j] > max_value:
                max_row = i
                max_column = j
                max_value = row[j]
    print(str(max_row) + ' ' + str(max_column))


if __name__ == '__main__':
    main()
