import shelve
import pyperclip
import sys


def main():
    mcbShelf = shelve.open('mcb')

    if len(sys.argv) == 3:
        if sys.argv[1].lower() == 'save':
            mcbShelf[sys.argv[2]] = pyperclip.paste()
        elif sys.argv[1].lower() == 'delete' and sys.argv[2] in mcbShelf:
            del mcbShelf[sys.argv[2]]


    elif len(sys.argv) == 2:
        if sys.argv[1].lower() == 'list':
            pyperclip.copy(str(list(mcbShelf.keys())))
        elif sys.argv[1] in mcbShelf:
            pyperclip.copy(mcbShelf[sys.argv[1]])
        elif sys.argv[1].lower() == 'delete':
            for el in list(mcbShelf.keys()):
                del mcbShelf[el]


    mcbShelf.close()


if __name__ == '__main__':
    main()
