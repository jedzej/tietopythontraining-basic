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
keyword = sys.argv
command = keyword[1].lower()
sub_command = keyword[2].lower()

if len(keyword) == 3 and command == 'save':
    mcbShelf[keyword[2]] = pyperclip.paste()
elif len(keyword) == 2:
    if command == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif keyword[1] in mcbShelf:
        pyperclip.copy(mcbShelf[keyword[1]])
elif len(keyword) == 3 and command == 'delete':
    if sub_command == 'all':
        mcbShelf.clear()
    elif keyword[2] in mcbShelf:
        del mcbShelf[keyword[2]]

mcbShelf.close()
