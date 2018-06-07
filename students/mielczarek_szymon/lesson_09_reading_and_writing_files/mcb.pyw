#! python3
import shelve
import pyperclip
import argparse


def print_shelf(shelf):
    for key, val in shelf.items():
        print("{}: {}".format(key, val))


def main():
    mcb_shelf = shelve.open('mcb')

    parser = argparse.ArgumentParser(
        description='Multiclipboard program to keep track of multiple '
                    'pieces of text.')

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-save',
                       action='store',
                       metavar='keyword',
                       help='Save clipboard to keyword.')
    group.add_argument('-list',
                       action='store',
                       metavar='keyword',
                       help='Loads keyword to clipboard.')
    group.add_argument('-list-all',
                       action='store_true',
                       help='Loads all keywords to clipboard.')
    group.add_argument('-delete',
                       action='store',
                       metavar='keyword',
                       help='Deletes a keyword from the shelf.')
    group.add_argument('-delete-all',
                       action='store_true',
                       help='Deletes all keywords from the shelf.')

    results = parser.parse_args()
    if results.save:
        mcb_shelf[results.save] = pyperclip.paste()
    elif results.list:
        pyperclip.copy(mcb_shelf[results.list])
    elif results.list_all:
        pyperclip.copy(str(list(mcb_shelf.keys())))
    elif results.delete:
        del mcb_shelf[results.delete]
    elif results.delete_all:
        mcb_shelf.clear()

    print_shelf(mcb_shelf)

    mcb_shelf.close()


if __name__ == "__main__":
    main()
