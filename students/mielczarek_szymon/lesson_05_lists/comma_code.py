def comma_items(a):
    """Comma items with 'and' inserted before the last item
    and return a string
    """
    a.insert(-1, 'and')
    return ', '.join(a[:-1]) + ' ' + a[-1]


if __name__ == "__main__":
    spam = ['apples', 'bananas', 'tofu', 'cats']
    print(comma_items(spam))
    # expected output: 'apples, bananas, tofu, and cats'
