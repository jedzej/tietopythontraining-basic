import re


def my_strip(string, char=" "):
    for_delete = "^([" + char + "]*)|([" + char + "]*)$"
    regex = re.compile(for_delete)
    return regex.sub("", string)


print(my_strip('yysome testyy', 'yy'))
print(my_strip('aa aa some test aa aa', 'aa'))
print(my_strip('o osome test', 'o'))
print(my_strip('some test eee', 'e'))
print(my_strip(',. some test .,', ','))
print(my_strip('  some test  '))
