import re


def like_strip(n_string, to_remove=" "):
    if to_remove != " ":
        return re.sub(to_remove, '', n_string)
    else:
        m = re.compile("^([" + to_remove + "]*) | ([" + to_remove + "]*)$")
        return m.sub('', n_string)


test = like_strip(input('String: '), input('To remove: '))
print(test)
