#!/usr/bin/env python3

desk_capacity = int(2)
total = 0

def desks_needed(stud_num):
  whole = int(stud_num / desk_capacity)
  left  = int(stud_num % desk_capacity)
  if(left!=0):
    whole = whole + 1
  return whole;



#print('Enter the number of students in group a')
students_a = int(input())

#print('Enter the number of students in group b')
students_b = int(input())

#print('Enter the number of students in group c')
students_c = int(input())

students_a = desks_needed(students_a)
students_b = desks_needed(students_b)
students_c = desks_needed(students_c)

#print('Group A needs {0:d} desks'.format(students_a))
#print('Group B needs {0:d} desks'.format(students_b))
#print('Group C needs {0:d} desks'.format(students_c))

#print('School needs {0:d} desks in total'.format(students_a+students_b+students_c))
print('{0:d}'.format(students_a+students_b+students_c))
