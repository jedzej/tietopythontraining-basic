def read_from_console():
    text = 'Write Number'
    a = float(input())
    b = float(input())
    c = float(input())
    print('Result\n', a + b + c)


def area():
    text = 'Write Number:\n'
    a = float(input(text))
    h = float(input(text))
    print('Result\n', a * h / 2)


def greet():
    a = input('Write Your Name\n')
    print('Hello, ' + a + '!')


def apple():
    n = int(input('Input number of students\n'))
    k = int(input('Input numer of apples\n'))
    apple_per_student = int(k / n)
    apples_left_in_basket = k % n
    print('How many apples per student - ' + str(
        apple_per_student) + '\nApples left in basket - ' + str(
        apples_left_in_basket))


def prev_and_next():
    number = int(input('Please write a number\n'))
    print('The next number for the number ' + str(number) + ' is ' + str(
        number + 1),
          '\nThe previous number for the number ' + str(number) + ' is ' + str(
              number - 1))


def calculate_desks_for_clas(children_in_class):
    if children_in_class % 2 == 0:
        desks_needed_for_class = children_in_class / 2
    else:
        desks_needed_for_class = int(children_in_class / 2) + 1
    return desks_needed_for_class


def desks():
    class1 = int(input('Write number of students in class1\n'))
    class2 = int(input('Write number of students in class2\n'))
    class3 = int(input('Write number of students in class3\n'))
    print(calculate_desks_for_clas(class1) + calculate_desks_for_clas(
        class2) + calculate_desks_for_clas(class3))


if __name__ == '__main__':
    # read_from_console()
    # area()
    # greet()
    # apple()
    # prev_and_next()
    # desks()
    pass
