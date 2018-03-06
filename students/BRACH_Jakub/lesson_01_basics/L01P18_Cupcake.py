#!/usr/bin/env python3
import math

print('Enter Dolar Price')
dolar = int(input())

print('Enter Cent Price')
cent = int(input())

print('Enter quantity')
qty =  int(input())

dolar_cost = dolar * qty
cent_cost  = cent  * qty

dolar_cost = dolar_cost + (cent_cost / 100)
cent_cost  = cent_cost % 100


print('Total will be {0:d}$ {1:02d}c'.format(dolar_cost, cent_cost))


  
