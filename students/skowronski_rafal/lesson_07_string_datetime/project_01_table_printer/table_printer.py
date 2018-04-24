def get_printable_table(table_data):
    column_lengths = [len(max(column, key=len)) for column in table_data]
    lines = []

    for row in zip(*table_data):
        words = []
        for k in range(len(row)):
            word = ' '.join([str(row[k]).rjust(column_lengths[k])])
            words.append(word)
        line = ' '.join(words)
        lines.append(line)

    return '\n'.join(lines)


def get_printable_table_v2(table_data):
    column_lengths = [len(max(column, key=len)) for column in table_data]
    return '\n'.join([' '.join([str(row[k]).rjust(column_lengths[k])
                                for k in range(len(row))])
                      for row in zip(*table_data)])


def print_table(table_data):
    print(get_printable_table(table_data))


def print_table_v2(table_data):
    print(get_printable_table_v2(table_data))


if __name__ == '__main__':
    table_data = [
        ['apples', 'oranges', 'cherries', 'banana'],
        ['Alice', 'Bob', 'Carol', 'David'],
        ['dogs', 'cats', 'moose', 'goose']
    ]

    print_table(table_data)
    print()
    print_table_v2(table_data)
