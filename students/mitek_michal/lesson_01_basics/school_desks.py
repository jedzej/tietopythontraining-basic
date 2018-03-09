
def calculate_number_of_desks_required():

    a = int(input("Provide number of students in first class "))
    b = int(input("Provide number of students in second class "))
    c = int(input("Provide number of students in third class "))

    print(a // 2 + b // 2 + c // 2 + a % 2 + b % 2 + c % 2)


calculate_number_of_desks_required()

