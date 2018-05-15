spam = ['apples', 'bananas', 'tofu', 'cats']


def coma_code(_list):
    _str = ''
    for item in _list:
        _str = _str + ' ' + str(item)
        if item != _list[-1]:
            _str = _str + ','
    return _str


print coma_code(spam)
