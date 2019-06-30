'''
Strong Password Detection
Write a function that uses regular expressions
to make sure the password string it is passed is
strong. A strong password is defined as one that is
at least eight characters long, contains both uppercase
and lowercase characters, and has at least one digit.
You may need to test the string against multiple regex
patterns to validate its strength.
'''
import re


def is_it_strong_password(password):
    passwordLengthRule = re.compile(r'^.{8,}$')
    res = passwordLengthRule.findall(password)
    if (res != []):
        passwordRule = re.compile(
            r'^(.*?([a-z]+).*?([A-Z]+).*?([0-9]+).*?)'
            r'|(.*?([A-Z]+).*?([a-z]+).*?([0-9]+).*?)'
            r'|(.*?([0-9]+).*?([a-z]+).*?([A-Z]+).*?)'
            r'|(.*?([0-9]+).*?([A-Z]+).*?([a-z]+).*?)'
            r'|(.*?([A-Z]+).*?([0-9]+).*?([a-z]+).*?)'
            r'|(.*?([a-z]+).*?([0-9]+).*?([A-Z]+).*?)$')
        res = passwordRule.findall(password)
        if res != []:
            print(password, " is strong")
            return True
        else:
            print(password, " is not strong")
            return False
    else:
        print("Password", password, "is too short.")


if __name__ == "__main__":
    is_it_strong_password("abc")
    is_it_strong_password("1Aa")
    is_it_strong_password("aaaaaaaAaaaa")
    is_it_strong_password("aaaaaaa1aaaa")
    is_it_strong_password("AAAAAAAAaAAA")
    is_it_strong_password("aaAaaaa1aa")
    is_it_strong_password("Aaaaa1aaaa")
    is_it_strong_password("1aaAaaaaaaa")
    is_it_strong_password("aa1Aaaaaaaa")
    is_it_strong_password("A1aaaaaaa")
    is_it_strong_password("a1AAAAAAAAAAA")
