#! python3
import sys
import shelve
import pyperclip

"""
mcb.pyw - Saves and loads pieces of text to the clipboard.
Usage:  py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
        py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
        py.exe mcb.pyw list - Loads all keywords to clipboard.
        py.exe mcb.pyw delete <keyword> - Deletes a keyword from the shelf.
        py.exe mcb.pyw delete - Deletes all keywords from the shelf.
"""


def print_shelf(shelf):
    for key, val in shelf.items():
        print("{}: {}".format(key, val))


def main(argv):
    mcb_shelf = shelve.open('mcb')

    # Save clipboard content.
    if len(argv) == 2:
        if argv[0].lower() == 'save':
            mcb_shelf[argv[1]] = pyperclip.paste()
        elif argv[0].lower() == 'delete':
            del mcb_shelf[argv[1]]
    elif len(argv) == 1:
        # List keywords and load content.
        if argv[0].lower() == 'list':
            pyperclip.copy(str(list(mcb_shelf.keys())))
        if argv[0].lower() == 'delete':
            mcb_shelf.clear()
        elif argv[0] in mcb_shelf:
            pyperclip.copy(mcb_shelf[argv[1]])

    print_shelf(mcb_shelf)

    mcb_shelf.close()


if __name__ == "__main__":
    main(sys.argv[1:])
