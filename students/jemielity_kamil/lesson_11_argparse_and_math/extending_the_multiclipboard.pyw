import shelve
import pyperclip
import argparse

parser = argparse.ArgumentParser(description='Short sample app')
group = parser.add_mutually_exclusive_group()

group.add_argument('-s', action='store',
                   dest="save",
                   help='Save clipboard content with a keyword')

group.add_argument('-d', action="store",
                   dest='delete',
                   help="Delete a keyword")

group.add_argument('-l', action="store_true",
                   default=False, dest='list',
                   help="Display list of keywords")

group.add_argument('-c', action="store_true",
                   default=False, dest='clear',
                   help="Delete all keywords")

group.add_argument('-g', action="store", dest='get',
                   help="Get a value of keyword")

args = parser.parse_args()

mcbShelf = shelve.open('mcb')

if args.save is not None:
    mcbShelf[args.save] = pyperclip.paste()
elif args.delete is not None:
    mcbShelf.pop(args.delete)
elif args.list is True:
    pyperclip.copy(str(list(mcbShelf.keys())))
elif args.clear is True:
    mcbShelf.clear()
elif args.get in mcbShelf:
    pyperclip.copy(mcbShelf[args.get])

mcbShelf.close()




