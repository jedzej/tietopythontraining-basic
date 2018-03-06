
def calculate_number_of_desks_required():

    a = int(input("Provide number of students in first class "))
    b = int(input("Provide number of students in second class "))
    c = int(input("Provide number of students in third class "))

    classes = [a, b, c]

    desks = []

    for students in classes:
        if check_if_number_of_students_is_even(students):
            desks.append(calculate_number_of_desks(students))
        else:
            desks.append(calculate_number_of_desks(students+1))

    print(int(sum(desks)))


def check_if_number_of_students_is_even(students):
    if students % 2 == 0:
        return True
    else:
        return False


def calculate_number_of_desks(students):
    return students / 2


calculate_number_of_desks_required()
