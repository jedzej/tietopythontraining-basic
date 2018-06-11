import os

path = 'Path\\to\\directory'

for foldername, _, filenames in os.walk(path):
    for file in filenames:
        path_to_file = os.path.join(foldername, file)
        file_size = os.path.getsize(path_to_file)
        if file_size > 100000000:
            print('FILENAME: ' + file + ' SIZE: ' +
                  str(file_size) +
                  ' bytes' + ' PATH: ' + path_to_file)
            # os.unlink(path_to_file)
