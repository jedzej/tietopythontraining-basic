#!/usr/bin/env python3

#print('Enter number of students')
students = int(input())
#print('Enter number of apples')
apples = int(input())

if( students>0 and  apples> 0):
  #print('Every student will get {0:d} apples. {1:d} will stay in the basket.'.format(apples/students, apples%students))
  print('{0:d}\n{1:d}'.format(apples//students, apples%students))
else:
  print('Invalid Data!')
