#!/usr/bin/env python3

print('Enter the number')
int = int(input())
int = int % 100

int = int / 10
print('Tens digit in this integer is: {0:d}'.format(int))

