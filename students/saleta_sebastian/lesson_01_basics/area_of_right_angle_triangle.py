def area_of_right_angle_triangle(basis, height):
    HALF_CONST = 0.5
    triangle_field = HALF_CONST * basis * height
    print('area of right-angled triangle is: {}'.format(triangle_field))

if __name__ == '__main__':
    basis = int(input())
    height = int(input())
    area_of_right_angle_triangle(basis, height)