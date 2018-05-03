import re

def validate_postal_code():
    code = input("Type Polish postal code: ")
    code = code.replace(" ","")
    pattern = re.search(r"\d{2}[-]\d{3}", code)
    if len(code) != 6 or code.isalpha() or code.isdigit():
        print("Incorrect postal code")
    else:
        print("Correct psotal code", pattern.group())

validate_postal_code()
