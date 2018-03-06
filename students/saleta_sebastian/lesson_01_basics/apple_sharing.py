def apple_sharing(students, apples):
    apples_per_student = apples // students
    rest = apples % students
    fruit = 'apples'
    if apples_per_student == 1:
        fruit = 'apple'
    print('Every student will get {} {}.'.format(apples_per_student, fruit))
    print('In basket will remain {} {}.'.format(rest, fruit))

if __name__ == '__main__':
    num_of_students = int(input())
    num_of_apples = int(input())
    apple_sharing(num_of_students, num_of_apples)
