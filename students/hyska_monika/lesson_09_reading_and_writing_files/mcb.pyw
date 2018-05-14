"""
Multiclipboard program
commands(sample commands are on mcb.bat file):
py [filename].pyw save [keyword]
    -- save copied text to clipboard with special keyword
py [filename].pyw [keyword]
    -- paste to clipboard  text for saved keyword
py [filename].pyw list
    -- copy keywords list
py [filename].pyw delete [keyword]
    -- delete saved text with keyword
py [filename].pyw delete all
    -- clear all keyword
"""
import shelve, pyperclip, sys


mcbShelf = shelve.open("mcb")

if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
    if sys.argv[2].lower() == 'all':
        mcbShelf.clear()
    elif sys.argv[2] in mcbShelf:
        del mcbShelf[sys.argv[2]]

mcbShelf.close()
