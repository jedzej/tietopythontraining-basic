import re
a = input()
b = a.split('.')
if len(b) > 1:
    print('0.' + str(b[1]))
else:
    print(0)
