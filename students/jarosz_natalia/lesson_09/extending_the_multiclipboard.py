#! python3
# mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
#        py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
#        py.exe mcb.pyw list - Loads all keywords to clipboard.

import shelve
import pyperclip
import sys


def main():
    mcb_shelf = shelve.open('mcb')

    # TODO: Save clipboard content.
    if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
            mcb_shelf[sys.argv[2]] = pyperclip.paste()
    # Extend the multiclipboard program in this so that it has a delete_all
    # command line argument that will delete all keyword from the shelf.
    elif len(sys.argv) == 2 and sys.argv[1].lower() == 'delete_all':
        print("test1")
        for element in list(mcb_shelf.keys()):
            del mcb_shelf[element]
    elif len(sys.argv) == 2:
        # TODO: List keywords and load content.
        if sys.argv[1].lower() == 'list':
            pyperclip.copy(str(list(mcb_shelf.keys())))
        elif sys.argv[1] in mcb_shelf:
            pyperclip.copy(mcb_shelf[sys.argv[1]])

    # Extend the multiclipboard program in this so that it has a delete
    # #<keyword> command line argument that will delete
    # a keyword from the shelf.
    elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
        if sys.argv[2] in mcb_shelf:
            del mcb_shelf[sys.argv[2]]

    mcb_shelf.close()


if __name__ == "__main__":
    main()
