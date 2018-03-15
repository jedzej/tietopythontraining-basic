# Solves problem 04 - Apple sharing


def solve_apple_sharing_problem():
    students_number = int(input('Enter students number (N): '))
    apples_number = int(input('Enter apples number (K): '))

    apples_per_student = apples_number // students_number
    apples_left = apples_number % students_number

    print(end='\n')
    print('Each student will get {0} apple(s).'.format(apples_per_student))
    print('Number of apples left in basket: {0}'.format(apples_left))

if __name__ == '__main__':
    solve_apple_sharing_problem()
