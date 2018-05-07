#!/usr/bin/env python3
"""To swap the two words exercise"""


def main():
    """Main function"""
    msg = input()
    space_pos = msg.find(' ')
    print('{} {}'.format(msg[space_pos + 1:], msg[:space_pos]))


if __name__ == '__main__':
    main()
