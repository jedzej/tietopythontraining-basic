import os


max_size = 104857600
source = "/home/rybaapau/test"


def deleting(folder):
    for foldername, subfolders, filenames in os.walk(folder):
        for filename in filenames:
            filename_path = os.path.join(foldername, filename)
            size = os.path.getsize(filename_path)
            if size > max_size:
                print("Big file: {} is {} bytes".format(filename_path, size))


if __name__ == '__main__':
    deleting(source)
    print('The end')
