#!/usr/bin/env python3

print('Enter number of students')
students = input()
print('Enter number of apples')
apples = input()

if( students>0 and  apples> 0):
  print('Every student will get {0:d} apples. {1:d} will stay in the basket.'.format(apples/students, apples%students))
else:
  print('Invalid Data!')
  