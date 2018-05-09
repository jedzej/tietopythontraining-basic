import re


def validate_strong_password(password):
    strong_password = False
    if password_length(password):
        if password_contains_lowercase_characters(password):
            if password_contains_uppercase_characters(password):
                if password_contains_digit(password):
                    strong_password = True
    return strong_password


def password_length(password):
    length_password_regex = re.compile(r'.{8,}')
    enough_password_length = length_password_regex.search(password)
    if enough_password_length is not None:
        return True
    else:
        return False


def password_contains_lowercase_characters(password):
    lowercase_characters_regex = re.compile(r'[a-z]+')
    lowercase_characters_found = lowercase_characters_regex.search(password)
    if lowercase_characters_found is not None:
        return True
    else:
        return False


def password_contains_uppercase_characters(password):
    uppercase_characters_regex = re.compile(r'[A-Z]+')
    uppercase_characters_found = uppercase_characters_regex.search(password)
    if uppercase_characters_found is not None:
        return True
    else:
        return False


def password_contains_digit(password):
    digit_characters_regex = re.compile(r'[\d]+')
    digit_characters_found = digit_characters_regex.search(password)
    if digit_characters_found is not None:
        return True
    else:
        return False


def main():
    password = "a123df&^%$g"
    if validate_strong_password(password):
        print("password is strong")
    else:
        print("password is weak")


if __name__ == "__main__":
    main()
