#!/usr/bin/env python3


import sys
import os
import copy
import shelve
import pyperclip


def print_usage():
    print(r'''Usage: mcb.pyw <action> <optional keyword>
                save   <keyword> - Saves clipboard to keyword.
                copy   <keyword> - Loads keyword to clipboard.
                delete <keyword> - Deletes keyword from database.
                list  - Loads all keywords to clipboard.
                print - Prints all keywords.
                purge - Deletes whole database.''')


def main():
    argc = len(sys.argv)

    if argc < 2 or argc > 3:
        print_usage()
        exit()

    mcb_shelf = shelve.open('mcb')
    action = sys.argv[1].lower()

    if argc == 2:
        if action == 'help':
            print_usage()
        if action == 'list':
            pyperclip.copy(str(list(mcb_shelf.keys())))
        elif action == 'print':
            print(str(list(mcb_shelf.keys())))
        elif action == 'purge':
            mcb_shelf.close()
            os.remove('mcb')
        else:
            print_usage()
    else:
        keyword = sys.argv[2].lower()

        if action  == 'save':
            mcb_shelf[keyword] = pyperclip.paste()
        elif action == 'copy':
            if keyword in mcb_shelf:
                pyperclip.copy(mcb_shelf[keyword])
            else:
                print("No such keyword!")
        elif action == 'delete':
            del mcb_shelf[keyword]
            # prevent shelf file size leak
            new_mcb = shelve.open('new_mcb')
            new_mcb.update(copy.deepcopy(dict(mcb_shelf)))
            mcb_shelf.close()
            os.remove('mcb')
            os.rename('new_mcb', 'mcb')
        else:
            print_usage()

    mcb_shelf.close()


if __name__ == "__main__":
    main()
