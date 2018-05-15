import shelve
import pyperclip
import sys


def main():
    mcb_shelf = shelve.open('multiclipboard')
    if len(sys.argv) == 3:
        if sys.argv[1].lower() == 'save':
            mcb_shelf[sys.argv[2]] = pyperclip.paste()
        elif sys.argv[1].lower() == 'delete':
            del mcb_shelf[sys.argv[2]]
    elif len(sys.argv) == 2:
        if sys.argv[1].lower() == 'list':
            pyperclip.copy(str(list(mcb_shelf.keys())))
        elif sys.argv[1].lower() == 'delete':
            mcb_shelf.clear()
        elif sys.argv[1] in mcb_shelf:
            pyperclip.copy(mcb_shelf[sys.argv[1]])
    mcb_shelf.close()


if __name__ == '__main__':
    main()
