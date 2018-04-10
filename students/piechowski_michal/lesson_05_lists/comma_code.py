#!/usr/bin/env python3


def join_list(strings_list):
    if not strings_list:
        return "List is empty"
    elif len(strings_list) == 1:
        return str(strings_list[0])
    else:
        return ", ".join(strings_list[:-1]) + " and " + strings_list[-1]


strings_list = ['apples', 'bananas', 'tofu', 'cats']
print(join_list(strings_list))
