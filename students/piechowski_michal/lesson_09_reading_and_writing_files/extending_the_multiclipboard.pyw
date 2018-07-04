#!/usr/bin/env python3

import pyperclip
import shelve
import sys


shelf_file = shelve.open("my_shelve")


def print_help_and_exit():
    print("Examples of parameters which this script can be called with:")
    print("save my_key")
    print("my_key")
    print("delete my_key")
    print("delete")
    exit()


def load_clipboard_from_shelve():
    if len(sys.argv) != 2:
        print_help_and_exit()

    key_name = sys.argv[1]
    if key_name in shelf_file:
        print("loading to clipboard text from: " + key_name)
        pyperclip.copy(shelf_file[key_name])
    else:
        print(str(key_name) + " doesn't exist, so loading empty string")
        pyperclip.copy("")


def load_keys_from_shelve():
    if len(sys.argv) != 2:
        print_help_and_exit()

    print("loading shelve keys to clipboard")
    pyperclip.copy(", ".join(shelf_file.keys()))


def save_clipboard_to_shelve():
    if len(sys.argv) != 3:
        print_help_and_exit()

    key_name = sys.argv[2]
    copied_text = pyperclip.paste()

    print("saving '" + copied_text + "' under: " + key_name)
    shelf_file[key_name] = copied_text


def delete_key_from_shelve():
    if len(sys.argv) == 2:
        print("deleting all")
        shelf_file.clear()
    else:
        key_name = sys.argv[2]
        print("deleting: " + key_name)
        if key_name in shelf_file:
            del shelf_file[key_name]
        else:
            print(str(key_name) + " doesn't exist, so can't be deleted")


def main():
    if len(sys.argv) == 1 or len(sys.argv) > 3:
        print_help_and_exit()

    options = {"list": load_keys_from_shelve,
               "save": save_clipboard_to_shelve,
               "delete": delete_key_from_shelve}

    if sys.argv[1] in options:
        options[sys.argv[1]]()
    else:
        load_clipboard_from_shelve()


if __name__ == "__main__":
    main()
