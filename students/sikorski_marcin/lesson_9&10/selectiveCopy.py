import shutil, os

extension = str(input("What file extesion are we looking? "))

def copyFilesWithExtension(location):
    numberOfCopiedFiles = 0
    location = os.path.abspath(location)

    for folderName, subFolders, fileNames in os.walk(location):
        for fileName in fileNames:
            if fileName.endswith('.' + extension):
                print(fileName)
                numberOfCopiedFiles += 1
            #shutil.copy(fileName, 'C:\\Users\\Haku\\Desktop\\Python\\copiedFiles')
    print("The number of copied files: " + str(numberOfCopiedFiles))

copyFilesWithExtension(r'C:\Users\Haku\Desktop\Python')
print('\nProgram finished working')
