def comma(tab):
    tab.insert(-1, 'and')
    return ', '.join(tab[:-1]) + ' ' + tab[-1]


spam = ['apples', 'bananas', 'tofu', 'cats']
print(comma(spam))
