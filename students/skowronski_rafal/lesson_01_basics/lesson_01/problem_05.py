# Solves problem 05 - Previous and next


def solve_previous_and_next_problem():
    number = int(input('Enter an integer number: '))

    print(end='\n')
    print('The previous number for the number {0} is {1}.'.format(
        number, number - 1))
    print('The next number for the number {0} is {1}.'.format(
        number, number + 1))

if __name__ == '__main__':
    solve_previous_and_next_problem()
