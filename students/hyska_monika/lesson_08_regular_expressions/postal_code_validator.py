"""
Postal code validator - postal code validator that checks if supplied
correct postal code: 25-894
- tests: postal_code_validator_pytest.py
"""
import re


def check_postal_code(postal_code):
    post_code_regex = re.compile(r'(\d{2})-(\d{3}$)')
    post_code_result = post_code_regex.match(postal_code)
    if post_code_result is not None:
        print("Postal code is valid.")
        return True
    else:
        print("Postal code isn't valid.")
        return False


def main():
    post_code = input('Put postcode: ')
    check_postal_code(post_code)


if __name__ == '__main__':
    main()
