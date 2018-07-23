import re

my_words = {}
for word in ['ADJECTIVE', 'NOUN', 'VERB', 'ADVERB']:
    my_words[word] = input('Enter %s: ' % word)

with open('madLibs.txt', 'r') as my_file:
    lines = my_file.read()
    lines = re.sub('ADJECTIVE', my_words['ADJECTIVE'], lines)
    lines = re.sub('NOUN', my_words['NOUN'], lines)
    lines = re.sub('VERB', my_words['VERB'], lines)
    lines = re.sub('ADVERB', my_words['ADVERB'], lines)

with open('madLibschanged.txt', 'w') as output:
    output.write(lines)
