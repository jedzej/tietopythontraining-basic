import re

password_regex = re.compile(r'''(

(?=.*?[a-z])   #at least one lowercase character 
(?=.*?[A-Z])   #at least one uppercase character
(?=.*?\d)      #at least one digit
(?=.{8,})      #minimum eight characters long

)''', re.VERBOSE)


def password_strength():
    password = input("Enter a password: ")
    mo = password_regex.search(password)
    if not mo:
        print("Invalid password")
        return False
    else:
        print("Correct password")
        return True


if __name__ == "__main__":
    password_strength()
