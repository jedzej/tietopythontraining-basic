class Sth:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


def shallow(object_one, object_two, attributes):
    for attr in attributes:

        if getattr(object_one, attr) != getattr(object_two, attr):
            print('Not equal')
        else:
            print('Equal')


def main():
    first = Sth(10, 10.0, 'first')
    second = Sth(10, 10.0, 'first')
    third = Sth(10, 10.0, 'third')
    attrs = ['x', 'y', 'z']
    shallow(first, second, attrs)
    shallow(first, third, attrs)


if __name__ == '__main__':
    main()
