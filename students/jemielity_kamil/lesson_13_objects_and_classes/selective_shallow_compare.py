
class Object1:
    name = 'John'
    surname = 'Travis'
    age = 10


class Object2:
    name = 'John'
    surname = 'Scott'
    age = 32


def shallow_compare(obj1, obj2, attr_list):
    for element in attr_list:
        if getattr(obj1, element) == getattr(obj2, element):
            print('Values of attr ' + element + ' are the same')
        else:
            print('Values of attr ' + element + ' are different')


object1 = Object1
object2 = Object2
list_of_attr = ['name', 'surname', 'age']

shallow_compare(object1, object2, list_of_attr)
