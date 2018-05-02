def print_table(table_data):

    for i in range(len(table_data[0])):
        for j in range(len(table_data)):
            longest = find_longest(table_data[j])
            print(table_data[j][i].rjust(longest), end='\t')
        print()


def find_longest(words):
    longest_word = ''
    for word in words:
        if len(longest_word) < len(word):
            longest_word = word
    return len(longest_word)


table = [['apples', 'oranges', 'cherry', 'banana'],
             ['Alice', 'Bob', 'Carola', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

'''
  apples Alice  dogs
 oranges   Bob  cats
cherries Carol moose
  banana David goose
'''
#print(check_length('adam'))
#print(find_longest(table[0]))
print_table(table)
