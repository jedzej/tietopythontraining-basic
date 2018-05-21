#! python3
# Usage: python.exe extending_the_multiclipboard.py save <keyword> - Saves clipboard to keyword.
#        python.exe extending_the_multiclipboard.py <keyword> - Loads keyword to clipboard.
#        python.exe extending_the_multiclipboard.py list - Loads all keywords to clipboard.
#        python.exe extending_the_multiclipboard.py delete <keyword> - delete keyword.
#        python.exe extending_the_multiclipboard.py delete - delete all keywords.

import shelve
import pyperclip
import sys

mcb_shelf = shelve.open('mcb')

if len(sys.argv) == 3:
    if sys.argv[1].lower() == 'save':
        mcb_shelf[sys.argv[2]] = pyperclip.paste()
    elif sys.argv[1].lower() == 'delete' and sys.argv[2] in mcb_shelf:
        del mcb_shelf[sys.argv[2]]
elif len(sys.argv) == 2:
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcb_shelf.keys())))
    elif sys.argv[1].lower() == 'delete':
        for key in mcb_shelf:
            del mcb_shelf[key]
    elif sys.argv[1] in mcb_shelf:
        pyperclip.copy(mcb_shelf[sys.argv[1]])

mcb_shelf.close()
