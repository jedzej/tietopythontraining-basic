source_file = 'file_to_be_modified.txt'
target_file = 'file_after_modification.txt'
words_to_be_replaced = ['ADJECTIVE', 'ADVERB', 'VERB', 'NOUN']

with open(target_file, 'w') as outfile:
    with open(source_file, 'r', encoding='utf-8') as infile:
        for line in infile:
            target_line = []
            for word in line.split():
                new_word = word
                for replace_word in words_to_be_replaced:
                    if word.find(replace_word) != -1:
                        print('Enter ', replace_word)
                        new_word = input()
                        new_word = word.replace(replace_word, new_word)
                        break
                target_line.append(new_word)
            outfile.write(' '.join(target_line) + '\n')
