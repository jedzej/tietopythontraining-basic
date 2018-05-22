import shelve
import sys
import pyperclip


mcbShelf = shelve.open('mcb')
if len(sys.argv) == 3:
    if sys.argv[1].lower() == 'save':
        mcbShelf[sys.argv[2]] = pyperclip.paste()
    elif sys.argv[1].lower() == 'delete':
        del mcbShelf[sys.argv[2]]

elif len(sys.argv) == 2:
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])

    if sys.argv[1].lower() == 'delete':
        for element in list(mcbShelf.keys()):
            del mcbShelf[element]

mcbShelf.close()
