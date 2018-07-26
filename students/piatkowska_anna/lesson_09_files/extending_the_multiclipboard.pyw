'''
Extending the Multiclipboard
Extend the multiclipboard program in this chapter
so that it has a delete <keyword> command line argument
that will delete a keyword from the shelf.
Then add a delete command line argument that will delete all keywords.
'''
#! python3
# mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
#        py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
#        py.exe mcb.pyw list - Loads all keywords to clipboard.
#        py.exe mcb.pyw delete <keyword> - delete keyword.
#        py.exe mcb.pyw delete - delete all keywords.

import shelve, pyperclip, sys


def multiclipboard():
    mcbShelf = shelve.open('mcb')
    # Save clipboard content.
    if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
        mcbShelf[sys.argv[2]] = pyperclip.paste()
    elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
        if sys.argv[2] in mcbShelf.keys():
            del mcbShelf[sys.argv[2]]
    elif len(sys.argv) == 2:
    # List keywords and load content.
        if sys.argv[1].lower() == 'list':
            pyperclip.copy(str(list(mcbShelf.keys())))
        elif sys.argv[1].lower() == 'delete':
            # delete all keywords
            for k in mcbShelf.keys():
                del mcbShelf[k]
        elif sys.argv[1] in mcbShelf:
            pyperclip.copy(mcbShelf[sys.argv[1]])
    mcbShelf.close()


if __name__ == "__main__":
    multiclipboard()