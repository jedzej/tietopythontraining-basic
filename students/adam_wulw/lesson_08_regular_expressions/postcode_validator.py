import re


def is_post_code_valid(my_post_code):
    r = re.compile(r'((^)|\s)(\d{2})\-\d{3}')
    if r.search(my_post_code) is None:
        return False
    return True


my_post_code = '69-100'

if is_post_code_valid(my_post_code):
    print('Post code OK')
else:
    print('Post code format is not valid\n')
