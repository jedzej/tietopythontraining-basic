#!/usr/bin/env python3

"""
mcb.pyw: a practice project:
"Extending the Multiclipboard" from:
https://automatetheboringstuff.com/chapter8/

The program saves and loads pieces of text to the clipboard.
Usage: ./mcb.pyw save <keyword> - Saves clipboard to keyword.
       ./mcb.pyw <keyword> - Loads keyword to clipboard.
       ./mcb.pyw list - Loads all keywords to clipboard.
       ./mcb.pyw delete <keyword> - Removes a keyword from the shelf
       ./mcb.pyw delete - Removes all keywords from the shelf
"""

__author__ = "Daniel Urtnowski"
__version__ = "0.1"


import shelve
import pyperclip
import sys


MCB_FILE_PATH = './mcb'


def main():

    args_cnt = len(sys.argv)

    if args_cnt > 1:
        mcb_shelf = shelve.open(MCB_FILE_PATH)
        cmd = sys.argv[1].lower()

        if args_cnt > 2:
            keyword = sys.argv[2]

            if cmd == 'save':
                # Save clipboard content
                mcb_shelf[keyword] = pyperclip.paste()

            elif cmd == 'delete':
                # Delete value stored for a given key
                del mcb_shelf[keyword]

        else:
            # List keywords and load content
            if cmd == 'list':
                # List all keywords
                pyperclip.copy(str(list(mcb_shelf.keys())))

            elif cmd == 'delete':
                # Delete stored content
                mcb_shelf.clear()

            else:
                keyword = sys.argv[1]

                if keyword in mcb_shelf:
                    # Load value stored for a given key
                    pyperclip.copy(mcb_shelf[keyword])

                else:
                    # Clear clipboard content
                    pyperclip.copy('')

        mcb_shelf.close()


if __name__ == '__main__':
    main()
