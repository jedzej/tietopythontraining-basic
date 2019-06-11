import shelve
import pyperclip
import sys

multiclipboard_shelf = shelve.open('multiclipboard')

if len(sys.argv) == 3:
    # save clipboard content
    if sys.argv[1].lower() == 'save':
        multiclipboard_shelf[sys.argv[2]] = pyperclip.paste()
    # delete clipboard content
    elif sys.argv[1].lower() == 'delete':
        del multiclipboard_shelf[sys.argv[2]]

elif len(sys.argv) == 2:
    # list keywords
    if sys.argv[1].lower() == 'list':
        print(list(multiclipboard_shelf.keys()))
        pyperclip.copy(str(list(multiclipboard_shelf.keys())))

    # clear clipboard
    elif sys.argv[1].lower() == 'clear':
        for key in multiclipboard_shelf.keys():
            del multiclipboard_shelf[key]
    # load content
    elif sys.argv[1]:
        pyperclip.copy(multiclipboard_shelf[sys.argv[1]])

multiclipboard_shelf.close()
