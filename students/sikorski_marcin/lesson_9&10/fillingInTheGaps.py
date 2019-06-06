import shutil, os, re

sequenceToUse = re.compile(r'^(spam)(\d)(.txt)')
ext = ".txt"


def nameLocator(location):
    listOfFiles = []
    for root, dirs, files in os.walk(location):
        if sequenceToUse in files:
            listOfFiles.append(os.path.join(root, sequenceToUse))
        return listOfFiles
    print(listOfFiles)

nameLocator(r'C:\Users\Haku\Desktop\Python\lesson_9')

