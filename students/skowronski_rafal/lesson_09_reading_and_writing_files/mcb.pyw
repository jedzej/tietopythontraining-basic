#! python3
# mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
#        py.exe mcb.pyw load <keyword> - Loads keyword to clipboard.
#        py.exe mcb.pyw list - Loads all keywords to clipboard.
#        py.exe mcb.pyw delete <keyword> - Deletes keyword.

import shelve
import pyperclip
import argparse


def _clipboard_save(keyword, mcb_shelf):
    mcb_shelf[keyword] = pyperclip.paste()


def _clipboard_list(keyword, mcb_shelf):
    shelf_entities = list(mcb_shelf.keys())
    pyperclip.copy(str(shelf_entities))


def _clipboard_delete(keyword, mcb_shelf):
    if keyword is not None:
        del mcb_shelf[keyword]
    else:
        mcb_shelf.clear()


def _clipboard_load(keyword, mcb_shelf):
    pyperclip.copy(mcb_shelf[keyword])


def _get_parser():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(help='Commands')

    save_parser = subparsers.add_parser(
        'save',
        help='Saves clipboard to keyword')
    save_parser.set_defaults(func=_clipboard_save)
    save_parser.add_argument('keyword', help='Keyword to save')

    list_parser = subparsers.add_parser(
        'list',
        help='Loads all keywords to clipboard')
    list_parser.set_defaults(func=_clipboard_list, keyword=None)

    delete_parser = subparsers.add_parser(
        'delete',
        help='Deletes keyword')
    delete_parser.set_defaults(func=_clipboard_delete, keyword=None)
    delete_parser.add_argument('keyword', help='Keyword to delete', nargs='?')

    # Added 'load' keyword to have consistency in commands
    load_parser = subparsers.add_parser(
        'load',
        help='Loads keyword to clipboard')
    load_parser.set_defaults(func=_clipboard_load)
    load_parser.add_argument('keyword', help='Keyword to load')

    return parser


if __name__ == '__main__':
    parser = _get_parser()
    args = parser.parse_args()

    with shelve.open('mcb') as mcb_shelf:
        args.func(args.keyword, mcb_shelf)
