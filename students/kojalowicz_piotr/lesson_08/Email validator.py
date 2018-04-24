import re


def valid_email(email):
    if len(email) > 7:
        match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+'
                         '(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email)
        if match is not None:
            return True
    return False


print(valid_email("My.email@buziaczek.com"))
print(valid_email("my.email"))
print(valid_email("my@email@buziaczek.com"))
print(valid_email("my...email@buziaczek.com"))
print(valid_email("my.email@Buziaczek.com"))
print(valid_email("my.email@buziaczek.com"))

