'''
Statement
Given a number n, followed by n lines of text,
print all words encountered in the text,
one per line.
The words should be sorted in descending order
according to their number of occurrences in the text,
and all words with the same frequency should be printed in
lexicographical order.
Hint. After you create a dictionary of the words and
their frequencies, you would like to sort it according
to the frequencies.
This can be achieved if you create a list whose elements are
tuples of two elements: the frequency of occurrence of a word
and the word itself. For example, [(2, 'hi'), (1, 'what'), (3, 'is')].
Then the standard list sort will sort a list of tuples,
with the tuples compared by the first element,
and if these are equal, by the second element.
This is nearly what is required in the problem.
'''


def measure_frequency():
    line_number = int(input("Enter number of lines: "))
    words = {}
    for i in range(line_number):
        line = input("Enter line of words separated by space: ").split()
        for word in line:
            words.setdefault(word, 0)
            words[word] += 1
    words_list = []
    for k, v in words.items():
        words_list.append(tuple([v, k]))
    words_list.sort(key=lambda val: val[1], reverse=False)
    words_list.sort(key=lambda val: val[0], reverse=True)
    print("List of words in order of occurences: ")
    for i in words_list:
        print(i[1])


if __name__ == "__main__":
    measure_frequency()
