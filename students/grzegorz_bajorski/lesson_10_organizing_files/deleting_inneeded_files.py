import os


max_size = 1024 * 1024 * 100

for filename in os.listdir():
    if os.path.getsize(filename) > max_size:
        print("File ", filename , "size", os.path.getsize(filename))
