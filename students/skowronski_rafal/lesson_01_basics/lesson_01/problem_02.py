# Calculates area of the right triangle


def print_area_of_right_triangle():
    base = float(input('Enter base: '))
    height = float(input('Enter height: '))

    area = 0.5 * base * height

    print('Area of the triangle: ', area)

if __name__ == '__main__':
    print_area_of_right_triangle()
