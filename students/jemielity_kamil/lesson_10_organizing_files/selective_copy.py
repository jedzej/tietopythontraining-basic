import os
import shutil

folder_path = 'C:\\Path\\to\\starting\\folder'
path_to_final_destination = 'C:\\Path\\to\\final\\destination'

extension = input('Write an extention(e.g .pdf): ')

for foldername, subfolders, filenames in os.walk(folder_path):
    for filename in filenames:
        if filename.endswith(extension):
            shutil.copy(os.path.join(foldername, filename), path_to_final_destination)
