#!/usr/bin/env python3


import re


def email_validator(val_string):
    multiple_dots_regex = re.compile(r'\.\.')

    last_at = val_string.rfind('@')
    # Address must contain at least one at sign
    if last_at == -1:
        return False

    local_part = val_string[:last_at]
    domain_part = val_string[last_at + 1:]

    # Address length limits
    if len(local_part) > 64 or len(domain_part) > 255:
        return False
    dns_labels = domain_part.split(".")
    for label in dns_labels:
        if len(label) > 63:
            return False

    if local_part[0] == '"' and local_part[-1] == '"':
        # Spaces, quotes, and backslashes may only exist when within quoted
        # strings and preceded by a backslash
        porblematic_chars = [' ', '"']
        for i, character in enumerate(local_part[1:-1]):
            if character in porblematic_chars:
                if local_part[i] != '\\':
                    return False
    else:
        # Multiple dots are not allowed if not quoted
        if multiple_dots_regex.search(local_part):
            return False

        # Restricted characters are not allowed if not quoted
        restricted_chars = ['"', '(', ')', ',', ':', ';', '<', '>', '@', '[',
                            '\\', ']']
        for character in restricted_chars:
            if character in local_part:
                return False

    # Multiple dots not allowed in domain part
    if multiple_dots_regex.search(domain_part):
        return False

    domain_regex = re.compile(r'''(
        ([a-zA-Z0-9][a-zA-Z0-9.-]+\.)+[a-zA-Z0-9]{2,4}
    )''', re.VERBOSE)
    return True if domain_regex.match(domain_part) else False


def main():
    print(email_validator('strange@example.com'))


if __name__ == "__main__":
    main()
