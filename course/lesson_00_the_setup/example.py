'''This is an example module to teach you about git and PyCharm use.

Don't worry if you don't understand the structure yet. First just add and
commit the file.

PyCharm should underline or highlight any errors in your code. If you put
a cursor there it will tell you what is wrong and even suggest a fix.
For example this comment is in wrong type of quotes. With my settings putting
a cursor there and pressing alt+enter then enter will fix this.

Use PyCharm rename function to rename the calls in the test module also, not
just in this file.
'''

# unused imports should be underlined
import sys
from os import *

def UglyCode():
    """Fix the function name and remove unreachable code.
    """
    print('something')
    return
    print('unreachable')

def MoreNonPep8CodeSum(a, b):
    """This comment is in wrong quotes and should be underlined."""
    return sum(a, b, 1)