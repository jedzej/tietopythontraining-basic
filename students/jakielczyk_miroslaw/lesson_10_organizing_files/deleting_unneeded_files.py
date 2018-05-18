import os

root_folder = 'folder_1'
print('Files that are bigger than 145KB')
for folder_name, sub_folders, file_names in os.walk(root_folder):
    for filename in file_names:
        file_size = os.path.getsize(os.path.join(folder_name, filename)) // 1024
        if file_size > 145:
            absolute_file_path = os.path.join(os.path.abspath(folder_name), filename)
            print(absolute_file_path, ' size= ', file_size, 'KB')
