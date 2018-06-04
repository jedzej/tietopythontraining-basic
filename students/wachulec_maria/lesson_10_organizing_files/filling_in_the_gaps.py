import os
import re
import shutil


def search_prefix_in_files_names(prefix):
    all_groups_list, list_of_numbers, names_list, result = [], [], [], None
    for file_name in os.listdir(PATH):
        result = re.search(re.compile('((' + prefix + ')(\d\d\d)(.*?)$)'),
                           file_name)
        if result is None:
            continue
        names_list.append(result.group(1))
        all_groups_list.append(list(result.groups()))
        list_of_numbers.append(result.group(3))
    if len(list_of_numbers) == 0:
        raise AttributeError("There are no file in the path")
    return len(result.group(3)), int(min(list_of_numbers)), sorted(
        names_list, reverse=False), all_groups_list


def create_new_names(surfix_len, start_surfix, names_list, split_text_list,
                     gap_in):
    new_names, step = {}, 1
    for i in range(len(names_list)):
        if gap_in == i + step:
            step += 1
        amount_null = surfix_len - len(str(start_surfix + i))
        new_names[names_list[i]] = (split_text_list[i][1] + '0' *
                                    amount_null + str(i + step) +
                                    split_text_list[i][3])
        print('Renaming "%s" to "%s"...' % (
            os.path.join(PATH, names_list[i]),
            os.path.join(PATH, new_names[names_list[i]])))
    return new_names


def change_name(list_of_all, new_names, base_path):
    answer = input('If you want to rename this file press "yes" or "y":\n')
    if answer.lower() == 'yes' or answer.lower() == 'y':
        print("Renaming...")
        for i in range(len(list_of_all)):
            shutil.move(os.path.join(base_path, list_of_all[i]),
                        os.path.join(base_path, 'r_'
                                     + new_names[list_of_all[i]]))
        for i in range(len(list_of_all)):
            shutil.move(os.path.join(base_path, 'r_'
                                     + new_names[list_of_all[i]]),
                        os.path.join(base_path, new_names[list_of_all[i]]))
    else:
        print("Cancel")


def run_filling_in_the_gaps(prefix, place_of_gap=None):
    len_of_surfix, start_number, names_list, list_of_all_groups =\
        search_prefix_in_files_names(prefix)
    new_names = create_new_names(len_of_surfix, start_number, names_list,
                                 list_of_all_groups, place_of_gap)
    change_name(names_list, new_names, PATH)


PATH = os.path.abspath('./files')
# RUN to close gap:
run_filling_in_the_gaps('spam')

# # RUN to add gap:
# run_filling_in_the_gaps('spam', 3)
