#!/usr/bin/env python3

print('Enter the number')
n = int(input())

if(n >99 and n <1000):
  summ = n /100;
  n = n % 100;
  
  summ = summ + (n /10) + (n%10);
  print('Summ on numbers is {0:d}'.format(summ))

else:
  print('Invalid Data!')
 
  
