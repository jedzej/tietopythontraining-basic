def get_attributes(obj, attr):
    return dict((i, getattr(obj, i)) for i in attr)


class Bmw:

    def __init__(self, model, engine):
        self.model = model
        self.engine = engine


def main():
    car = Bmw('e36', 2.5)
    attributes = ['model', 'engine']
    att_dict = get_attributes(car, attributes)
    print(att_dict)


if __name__ == '__main__':
    main()
