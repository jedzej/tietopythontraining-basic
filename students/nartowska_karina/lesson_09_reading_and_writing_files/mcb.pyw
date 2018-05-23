import shelve
import sys
import pyperclip


mcbShelf = shelve.open('mcb')
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
    del mcbShelf[sys.argv[2]]

if len(sys.argv) == 2 and sys.argv[1].lower() == 'list':
    pyperclip.copy(str(list(mcbShelf.keys())))
elif len(sys.argv) == 2 and sys.argv[1] in mcbShelf:
    pyperclip.copy(mcbShelf[sys.argv[1]])
elif len(sys.argv) == 2 and sys.argv[1].lower() == 'delete':
    for element in list(mcbShelf.keys()):
        del mcbShelf[element]

mcbShelf.close()
