#!/usr/bin/python

import re

file = open('fileToCheck.txt')
text = file.read()
file.close()

regex = re.compile(r'(ADJECTIVE)|(NOUN)|(VERB)')

for i in regex.findall(text):
    for j in i:
        if j != '':
            reg = re.compile(r'{}'.format(j))
            substituteText = input('Enter the substitute for %s: ' %j)
            text = reg.sub(substituteText, text, 1)

print(text)

file = open('newText', 'w')
file.write(text)
file.close()