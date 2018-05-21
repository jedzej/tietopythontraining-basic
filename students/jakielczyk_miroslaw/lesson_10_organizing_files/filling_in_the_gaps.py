import os
import re
import shutil

source_folder = 'spam_folder'
original_spam_folder = 'reference_spam_folder'

if not os.path.exists(source_folder):
    print('Creating', source_folder)
    os.makedirs(source_folder)

print('Removing content of spam_folder')
shutil.rmtree(source_folder)

print('Restoring original content of spam_folder')
shutil.copytree(original_spam_folder, source_folder)

prefix = 'spam'
regex_expression = re.compile(r'^spam\d{3}.txt$')

file_index = 0
for filename in os.listdir(source_folder):
    mo = regex_expression.search(filename)
    if mo is not None:
        file_index += 1

        correct_file_name = prefix + '0' * (3 - len(str(file_index))) + str(file_index) + '.txt'

        if filename != correct_file_name:
            print(filename, '->', correct_file_name)
            shutil.move(os.path.join(source_folder, filename),
                        os.path.join(source_folder, correct_file_name))
