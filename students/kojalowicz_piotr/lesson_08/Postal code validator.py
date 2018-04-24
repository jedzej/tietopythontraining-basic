import re


def valid_postal_code(postal_code):
    if re.compile(r'^\d{2}-\d{3}$').match(postal_code):
        return True
    return False


print(valid_postal_code("@@@@@@"))
print(valid_postal_code("@@-@@@"))
print(valid_postal_code("QQ-@@@"))
print(valid_postal_code("11-111"))

