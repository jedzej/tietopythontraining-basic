#!/usr/bin/env python3
n = int(input())
if(n > 99 and n < 1000):
  summ = n // 100;
  n = n % 100;
  summ = summ + (n //10) + (n%10);
  print('{0:d}'.format(int(summ)))
else:
  print('Invalid Data!')
 
  
