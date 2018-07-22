class Books:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year


def shallow_compare(object1, object2, attributes):
    for attribute in attributes:
        if getattr(object1, attribute) != getattr(object2, attribute):
            return False
        else:
            return True


def main():
    book1 = Books("Uwiklanie", "Zygmunt Miloszewski", 2007)
    book2 = Books("Uwiklanie", "Zygmunt Miloszewski", 2007)
    book3 = Books("Hasztag", "Remigiusz Mroz", 2018)
    print("Book1: author: {}, title: {}, year: {}".format(book1.author,
                                                          book1.title,
                                                          book1.year))
    print("Book2: author: {}, title: {}, year: {}".format(book2.author,
                                                          book2.title,
                                                          book2.year))
    print("Book3: author: {}, title: {}, year: {}".format(book3.author,
                                                          book3.title,
                                                          book3.year))
    attributes_list = ['title', 'author', 'year']
    print("Are book 1 and book 2 equal? " + str(
        shallow_compare(book1, book2, attributes_list)))
    print("Are book 1 and book 3 equal? " + str(
        shallow_compare(book1, book3, attributes_list)))


if __name__ == "__main__":
    main()
