#! python3
"""
mcb.pyw - Saves and loads pieces of text to the clipboard
Usage:
    py.exe mcb.pyw save <keyword> - Saves clipboard to keywords
    py.exe mcb.pyw <keyword> - Loads keyword to clipboard
    py.exe mcb.pyw delete <keyword> - Deletes a keyword from the shelf
    py.exe mcb.pyw list - Loads all keywords to clipboard
    py.exe mcb.pyw delete - Deletes al keywords from the shelf
"""

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

if len(sys.argv) == 3:

    if sys.argv[1].lower() == 'save':
        # Save clipboard content

        mcbShelf[sys.argv[2]] = pyperclip.paste()

    elif sys.argv[1].lower() == 'delete':
        # delete content for the keyword

        del mcbShelf[sys.argv[2]]

elif len(sys.argv) == 2:
    # List keywords and load content

    if sys.argv[1].lower() == 'list':

        pyperclip.copy(str(list(mcbShelf.keys())))

    elif sys.argv[1].lower() == 'delete':

        mcbShelf.clear()

    elif sys.argv[1] in mcbShelf:

        pyperclip.copy(mcbShelf[sys.argv[1]])

mcbShelf.close()
