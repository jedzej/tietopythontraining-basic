# Solves problem 06 - School desks


def ceil_division(dividend, divisor):
    return -(-dividend // divisor)


def solve_school_desks_problem():
    STUDENTS_PER_DESK = 2

    students_first_group = int(
        input('Enter number of students in first classroom: '))
    students_second_group = int(
        input('Enter number of students in second classroom: '))
    students_third_group = int(
        input('Enter number of students in third classroom: '))

    print(end='\n')

    print('Total number of needed desks is {0}.'.format(
        ceil_division(students_first_group, STUDENTS_PER_DESK) +
        ceil_division(students_second_group, STUDENTS_PER_DESK) +
        ceil_division(students_third_group, STUDENTS_PER_DESK)))

if __name__ == '__main__':
    solve_school_desks_problem()
