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


def number():
    while True:
        try:
            number = int(input('Please write intiger number:\n'))
            print(number % 10)
            break
        except ValueError:
            print('Write intiger number You ...:')


# It does not support negative numbers. If I need to convert the number to a
# string and display the last character.

def tens_digit():
    number = int(input('Please write intiger number:\n'))
    print('The tens digit of Your number is:\n' + str((number % 100 // 10)))


def three_digits():
    number = input('Please write three-digit number:\n')
    # suma = 0
    # for cyfra in number:
    #     suma += cyfra
    suma = sum([int(cyfra) for cyfra in number])
    print('Your suma is:\n {}'.format(suma))


def fractional_part():
    number = float(input('Write intiger number:\n'))
    number1 = int(number)
    print(number - number1)


def first_digit_after_decimal_point():
    number = float(input('Write Your positive real number:\n'))
    number1 = int(number)
    suma = (number - number1)
    print('Your score:\n', (suma * 10))


def car_route():
    km_by_car = float(input('Write how many km Your car can ride:\n'))
    route_all_km = float(input('Write how many km has entire route:\n'))
    print('You need ', (route_all_km / km_by_car), 'days for this route')


# def digital_clock():
#     passed_minutes = int(input('Write hom many minutes it has passed\n'))
#     minutes_after_midnight = passed_minutes / 60
#     minutes100 = int(minutes_after_midnight * 100) / 100
#     score = int(minutes100)
#     score1 = (minutes100 - score) * 100
#     score2 = int(score1)
#     print(score,'',score2)

def digital_clock_():
    passed_minutes = int(input('Write how many minutes it has passed\n'))
    hours = int((passed_minutes / 60) % 24)
    minutes = passed_minutes % 60
    print('Time: ', hours, '', minutes)


def cupcake_cost():
    price = float(input('Please write the prise for the cupcakes:\n'))
    dolars = int(price)
    cents = price - dolars
    how_many_cupcakes = int(input(
        'Please write how many cupcakes You want to buy:\n'))
    final_dolars = dolars * how_many_cupcakes
    final_cents = cents * how_many_cupcakes
    final_cents_plus = (final_cents - int(final_cents))* 100
    print('For', how_many_cupcakes, 'cupcakes You should pay',
          (final_dolars + int(final_cents)), 'dolars and ',
          int(final_cents_plus)), 'cents'


def clock_face_1():
    h = int(input('Please write hours:\n'))
    m = int(input('Please write minutes:\n'))
    s = int(input('Please write seconds:\n'))
    second = (h * 3600 + m * 60 + s)
    print((second * 360) / 43200)

if __name__ == '__main__':
    # read_from_console()
    # area()
    # greet()
    # apple()
    # prev_and_next()
    # desks()
    # number()
    # tens_digit()
    # three_digits()
    # fractional_part()
    # first_digit_after_decimal_point()
    # car_route()
    # digital_clock()
    # cupcake_cost()
    # clock_face_1()
    pass
