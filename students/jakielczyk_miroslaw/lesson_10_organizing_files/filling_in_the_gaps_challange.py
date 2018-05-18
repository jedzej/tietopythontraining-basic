import os
import re
import shutil


def creating_folder(folder_name):
    if not os.path.exists(temp_folder):
        print('Creating', folder_name)
        os.makedirs(folder_name)


def removing_folder(folder_name):
    if os.path.exists(folder_name):
        print('Removing', folder_name)
        shutil.rmtree(folder_name)


def copying_folder(reference_folder, destination_folder):
    print('Copying', reference_folder, 'to', destination_folder)
    shutil.copytree(reference_folder, destination_folder)


source_folder = 'spam_folder_challenge'
temp_folder = 'temp_folder'
original_spam_folder = 'reference_spam_folder_challenge'

removing_folder(source_folder)
copying_folder(original_spam_folder, source_folder)
creating_folder(temp_folder)

prefix = 'spam'

begin_gap_index = 5
number_of_gaps = 7

file_index = 0
regex_expression = re.compile(r'^spam\d{3}.txt$')
for filename in os.listdir(source_folder):
    mo = regex_expression.search(filename)
    if mo is not None:
        file_index += 1

        correct_file_name = prefix + '0' * (3 - len(str(file_index))) + str(file_index) + '.txt'

        if filename == correct_file_name:
            if file_index >= begin_gap_index:
                destination_file_name = prefix + '0' * (3 - len(str(file_index + number_of_gaps))) + str(
                    file_index + number_of_gaps) + '.txt'
                print(filename, '->', destination_file_name)

                shutil.copy(os.path.join(source_folder, filename),
                            os.path.join(temp_folder, destination_file_name))

            else:
                shutil.copy(os.path.join(source_folder, filename),
                            os.path.join(temp_folder, filename))

removing_folder(source_folder)
copying_folder(temp_folder, source_folder)
removing_folder(temp_folder)
