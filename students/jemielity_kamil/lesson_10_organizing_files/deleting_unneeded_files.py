import os

path = 'Path\\to\\directory'

for foldername, subfolders, filenames in os.walk(path):
    for file in filenames:
        path_to_file = os.path.join(foldername, file)
        if os.path.getsize(path_to_file) > 100000000:
            print('FILENAME: ' + file + ' SIZE: '
                  + str(os.path.getsize(path_to_file)) + ' bytes' + ' PATH: ' + path_to_file)
            # os.unlink(path_to_file)
