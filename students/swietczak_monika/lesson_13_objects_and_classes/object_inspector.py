class Books:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year


def object_inspector1(some_object):
    attributes = dir(some_object)
    return dict((key, getattr(some_object, key)) for key in attributes)


def object_inspector2(some_object):
    attributes = dir(some_object)
    return dict((key, getattr(some_object, key)) for key in attributes
                if isinstance(getattr(some_object, key), (int, float, str)))


def main():
    ksiazka = Books("Hasztag", "Remigiusz Mroz", 2018)
    print(object_inspector1(ksiazka))
    print(object_inspector2(ksiazka))


if __name__ == '__main__':
    main()
