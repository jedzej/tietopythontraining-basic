#!/usr/bin/env python3
import math
dolar = int(input())
cent = int(input())
qty =  int(input())

dolar_cost = dolar * qty
cent_cost  = cent  * qty
dolar_cost = dolar_cost + (cent_cost // 100)
cent_cost  = cent_cost % 100

print('{0:d} {1:02d}'.format(dolar_cost, cent_cost))

  
