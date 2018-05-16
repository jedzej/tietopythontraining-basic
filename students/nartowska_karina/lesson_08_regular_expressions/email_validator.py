import re


def email_validator(email):
    r_email = re.compile(r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)')
    if r_email.match(email):
        return 1


def main():
    set_of_emails = ("karinanartowska",
                     "karina@nartowska@pl",
                     ".karina@.pl",
                     "karina.@nartowska.pl",
                     "k.a.r.i.n.a@n.pl",
                     "karina@nartowska.pl")
    for email in set_of_emails:
        if email_validator(email):
            print(email + " is email")


if __name__ == "__main__":
    main()
