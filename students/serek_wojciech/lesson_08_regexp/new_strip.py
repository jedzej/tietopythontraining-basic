#!/usr/bin/env python3
"""Strip method exercise"""
import re


def new_strip(text, to_remove=' '):
    """New version of strip method"""
    regexp = re.compile("^([" + to_remove + "]*) | ([" + to_remove + "]*)$")
    return regexp.sub('', text)


def main():
    """Main function"""
    test_str_1 = " This is just a sample text"

    print(new_strip(test_str_1, ' This'))
    print(new_strip(test_str_1))


if __name__ == '__main__':
    main()
