def apple_sharing():
    students = int(input())
    apples = int(input())
    apples_per_student = apples // students
    rest = apples % students
    fruit = 'apples'

    if apples_per_student == 1:
        fruit = 'apple'

    print('Every student will get {} {}.'.format(apples_per_student, fruit))
    print('In basket will remain {} {}.'.format(rest, fruit))


if __name__ == '__main__':
    apple_sharing()
