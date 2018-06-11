import os
import shutil

FOLDER_PATH = 'C:\\Path\\to\\starting\\folder'
PATH_TO_FINAL_DESTINATION = 'C:\\Path\\to\\final\\destination'

extension = input('Write an extention(e.g .pdf): ')

for foldername, _, filenames in os.walk(FOLDER_PATH):
    for filename in filenames:
        if filename.endswith(extension):
            shutil.copy(os.path.join(foldername, filename),
                        PATH_TO_FINAL_DESTINATION)
