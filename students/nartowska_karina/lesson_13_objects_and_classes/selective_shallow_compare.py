class Animal:
    def __init__(self, kind, name, age):
        self.kind = kind
        self.name = name
        self.age = age


def compare_objects(obj_1, obj_2, atr_names):
    atr_obj_1 = []
    atr_obj_2 = []
    for j in atr_names:
        atr_obj_1.append(getattr(obj_1, j))
        atr_obj_2.append(getattr(obj_2, j))
    if atr_obj_1 != atr_obj_2:
        print("The attributes are different.")
    else:
        print("The attributes are equal.")


def main():
    animal_1 = Animal("shark", "Edward", 5)
    animal_2 = Animal("turtle", "Franklin", 100)
    compare_objects(animal_1, animal_2, ["kind", "name", "age"])


if __name__ == '__main__':
    main()
