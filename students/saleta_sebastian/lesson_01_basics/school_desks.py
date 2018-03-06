def smallest_num_of_desks(students_in_a_class,
                          students_in_b_class, students_in_c_class):
    if (students_in_a_class % 2 == 0):
        tables_in_class_a = students_in_a_class / 2
    else:
        tables_in_class_a = students_in_a_class // 2 + 1
    if (students_in_b_class % 2 == 0):
        tables_in_class_b = students_in_b_class / 2
    else:
        tables_in_class_b = students_in_b_class // 2 + 1

    if (students_in_c_class % 2 == 0):
        tables_in_class_c = students_in_c_class / 2
    else:
        tables_in_class_c = students_in_c_class // 2 + 1

    tables = tables_in_class_a + tables_in_class_b + tables_in_class_c
    print('School have to buy {} tables'.format(tables))

if __name__ == '__main__':
    num_of_students_in_a_class = int(input())
    num_of_students_in_b_class = int(input())
    num_of_students_in_c_class = int(input())
    smallest_num_of_desks(num_of_students_in_a_class,num_of_students_in_b_class,
                          num_of_students_in_c_class)

