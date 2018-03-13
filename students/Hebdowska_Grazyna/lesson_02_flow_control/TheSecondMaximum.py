m1 =  n = int(input('N: '))
m2 = 0
while n != 0:
    n = int(input('N: '))    
    if m1 < n:
       m2 = m1
       m1 = n
    elif m2 < n and n < m1:
       m2 = n

print(m2)

  
    
