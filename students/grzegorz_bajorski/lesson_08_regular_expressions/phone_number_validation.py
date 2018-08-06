import re


print("Provide phone number")
phone_number = input(str())

phone = re.compile(r'^(\+\d{1,3} ?)?\d{3}([ -]?\d{3}){2}$')
if phone.match(phone_number) is not None:
    print("Number is OK")
else:
    print("Wrong format")
