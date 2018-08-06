import re


print("Enter post code")
post_code = input(str())

code = re.compile(r'^\d{2}-\d{3}$')
if code.match(post_code) is not None:
    print("Post code is OK")
else:
    print("Invalid syntex")
