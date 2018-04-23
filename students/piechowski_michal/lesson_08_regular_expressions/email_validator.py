#!/usr/bin/env python3

import re


def is_valid(email):
    try:
        local_part, domain = email.split("@")
    except ValueError:
        return False

    if (len(local_part) < 0 or len(local_part) > 64 or
            len(domain) < 0 or len(domain) > 255):
        return False

    if (re.compile(r'.*\.\.').match(local_part) or
            re.compile(r'.*\.\.').match(domain)):
        return False

    if re.compile(r'^\.|.*\.$').match(local_part):
        return False

    if re.compile(r'^-|.*-$').match(domain):
        return False

    return True


def main():
    potential_mails = ("Ice@Cream.com", "icecream", "Ice@Cream@com",
                       "I..ce@Cream.com", "Ice@Cream..com", ".Ice@Cream.com",
                       "Ice.@Cream.com", "Ice@-Cream.com", "Ice@Cream.com-")
    for mail in potential_mails:
        if is_valid(mail):
            print("Mail: " + mail + " is valid")
        else:
            print("Mail: " + mail + " is not valid")


if __name__ == "__main__":
    main()
