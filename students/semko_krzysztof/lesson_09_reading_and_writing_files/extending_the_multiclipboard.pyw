"""
Extend the multiclipboard program in this chapter so that
it has a delete <keyword> command line argument that will
delete a keyword from the shelf. Then add a delete
command line argument that will delete all keywords.
"""

import shelve
import pyperclip
import sys


def menu():
    print("options:")
    print("save|list|delete|show")


def main():
    ext_mcb = shelve.open("ext_mcb")
    if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
        ext_mcb[sys.argv[2]] = pyperclip.paste()
    elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
        del ext_mcb[sys.argv[2]]
    elif len(sys.argv) == 2:
        if sys.argv[1].lower() == 'list':
            pyperclip.copy(str(list(ext_mcb.values())))
        elif sys.argv[1].lower() == 'save':
            ext_mcb[str(pyperclip.paste())] = pyperclip.paste()
        elif sys.argv[1].lower() == 'show':
            for i in ext_mcb:
                print(str(ext_mcb[i]))
        elif sys.argv[1].lower() == 'delete':
            for i in ext_mcb:
                del ext_mcb[i]
        elif sys.argv[1] in ext_mcb:
            pyperclip.copy(ext_mcb[sys.argv[1]])
    elif len(sys.argv) == 1:
        menu()

    ext_mcb.close()


if __name__ == '__main__':
    main()
