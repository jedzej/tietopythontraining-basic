def swap_columns(table = [], form_swap = int, to_swap = int):
    copy_table = table
    for row in range(table.count(table)):
        copy_table[row][form_swap] = 'tt'
        copy_table[row][to_swap] = 'oo'
    return copy_table



def main():
    param_table = input().split()
    rows = int(param_table[0])
    columns = int(param_table[1])
    table = []
    for row in range(rows):
        table.append([0]*columns)
    for row in range(rows):
        row_elemnts = input().split()
        for column in range(columns):
            table[row][column] = row_elemnts[column]
    param_swap = input().split()
    form_swap = int(param_swap[0])
    to_swap = int(param_swap[1])
    new_table = swap_columns(table, form_swap, to_swap)
    graf = ''
    for row in range(rows):
        for column in range(columns):
            graf += str(new_table[row][column]) + ' '
        graf += '\n'
    print(graf)
    print(table)
    print(new_table)



if __name__ == '__main__':
    main()