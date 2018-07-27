import re


def strong_password(password):
    strong = (len(password) >= 8 and
              re.compile(r'.*[a-z]').match(password) and
              re.compile(r'.*[A-Z]').match(password) and
              re.compile(r'.*\d').match(password) and
              re.compile(r'.*\W|.*_').match(password))
    if strong:
        return True
    else:
        return False


print(strong_password("hakunamatata"))
print(strong_password("HakunaMatata"))
print(strong_password("HakunaMatata777"))
print(strong_password("Hakuna_Matata777"))
