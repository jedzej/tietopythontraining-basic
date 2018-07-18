class Bmw:

    def __init__(self, model, engine):
        self.model = model
        self.engine = engine


def compare_objects(obj1, obj2, attributes):
    for attribute in attributes:
        if getattr(obj1, attribute) != getattr(obj2, attribute):
            return False

    return True


def main():
    attr = ['model', 'engine']
    first_beta = Bmw('e30', 1.8)
    second_beta = Bmw('e36', 2.0)
    comp_cars = compare_objects(first_beta, second_beta, attr)
    print('compare {} with {} - is equal: {}'.format(
        first_beta.model,
        second_beta.model,
        comp_cars
    ))


if __name__ == '__main__':
    main()
