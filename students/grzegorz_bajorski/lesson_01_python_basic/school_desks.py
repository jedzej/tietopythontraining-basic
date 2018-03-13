print('Enter number of students in first class')
class1 = int(input())

print('Enter number of students in second class')
class2 = int(input())

print('Enter number of students in third class')
class3 = int(input())

desk_in_class1 = (class1 // 2) + (class1 % 2)
desk_in_class2 = (class2 // 2) + (class2 % 2)
desk_in_class3 = (class3 // 2) + (class3 % 2)

total_desk = desk_in_class1 + desk_in_class2 + desk_in_class3

print ('Total number of desks is ' + str(total_desk))
