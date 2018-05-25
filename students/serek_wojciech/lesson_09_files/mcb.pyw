#!/usr/bin/env python3
"""Extending multiclipboard
    # mcb.pyw - Saves and loads pieces of text to the clipboard.
    # Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
    #        py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
    #        py.exe mcb.pyw list - Loads all keywords to clipboard.
    #        py.exe mcb.pyw delete <keyword> - delete keyword.
    #        py.exe mcb.pyw delete all - delete all keywords.
"""

import shelve
import sys
import pyperclip


def main():
    """Main function"""

    mcb_shelf = shelve.open('mcb')

    if len(sys.argv) == 3:
        if sys.argv[1].lower() == 'save':
            mcb_shelf[sys.argv[2]] = pyperclip.paste()
        elif sys.argv[1].lower() == 'delete':
            if sys.argv[2].lower() == 'all':
                mcb_shelf.clear()
            else:
                try:
                    del mcb_shelf[sys.argv[2]]
                except KeyError:
                    pass
    elif len(sys.argv) == 2:
        # List keywords and load content.
        if sys.argv[1].lower() == 'list':
            pyperclip.copy(str(list(mcb_shelf.keys())))
        elif sys.argv[1] in mcb_shelf:
            pyperclip.copy(mcb_shelf[sys.argv[1]])

    mcb_shelf.close()


if __name__ == '__main__':
    main()
