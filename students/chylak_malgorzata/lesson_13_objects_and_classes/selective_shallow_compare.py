class ObjectOne:
    cat = 'Ragdoll'
    colour = 'white'
    age = 2


class ObjectTwo:
    cat = 'Maine Coon'
    colour = 'gray'
    age = 6


def shallow_compare(one, two, attr_list):
    for element in attr_list:
        if getattr(one, element) == getattr(two, element):
            print('Values of attributes ' + element + ' are the same')
        else:
            print('Values of attributes ' + element + ' are different')


one = ObjectOne
two = ObjectTwo
list_of_attributes = ['cat', 'colour', 'age']

shallow_compare(ObjectOne, ObjectTwo, list_of_attributes)
