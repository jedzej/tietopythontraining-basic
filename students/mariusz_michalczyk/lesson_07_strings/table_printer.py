table_data = [['apples', 'oranges', 'cherries', 'banana'],
              ['Alice', 'Bob', 'Carol', 'David'],
              ['dogs', 'cats', 'moose', 'goose']]


def print_table(table_data):
    col_width, max_word_len = get_maxs(table_data)
    for i in range(col_width):
        for col in table_data:
            print(str(col[i]).rjust(int(max_word_len)), end=' ')
        print('')


def get_maxs(table_data):
    col_widths = []
    words = []
    for inner_list in table_data:
        col_widths.append(len(inner_list))
        for word in inner_list:
            words.append(len(word))
    return max(col_widths), max(words)


if __name__ == '__main__':
    print_table(table_data)
