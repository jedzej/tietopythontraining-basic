# mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
#        py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
#        py.exe mcb.pyw list - Loads all keywords to clipboard.
#        py.exe mcb.pyw delete <keyword> - selected keyword deleted from shelf
#        py.exe mcb.pyw delete - all keyword deleted from shelf

import shelve
import pyperclip
import sys

mcbShelf = shelve.open('mcb')

if len(sys.argv) == 3:
    if sys.argv[1].lower() == 'save':
        mcbShelf[sys.argv[2]] = pyperclip.paste()
    elif sys.argv[1].lower() == 'delete':
        if sys.argv[2] in mcbShelf:
            print("{0} deleted from multiclipboar!".format(sys.argv[2]))
            del mcbShelf[sys.argv[2]]
        else:
            print("{0} does not exist in multiclipboar!".format(sys.argv[2]))

elif len(sys.argv) == 2:
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    if sys.argv[1].lower() == 'delete':
        mcbShelf.clear()
        print("All data in multiclipboard was deleted!")
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])

mcbShelf.close()
