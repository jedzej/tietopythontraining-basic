import shutil, os

def fileSize(location):

    for folderName, subFolders, fileNames in os.walk(location):
        for fileName in fileNames:
            fileSize = os.path.getsize(fileName)
            if int(fileSize) > 5000000:
                print(fileName)
                #os.unlink(fileName)


fileSize(r'C:\Users\Haku\Desktop\Python\lesson_9')

print('\nFile was deleted')
