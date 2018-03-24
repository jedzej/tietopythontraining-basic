"""
description:
    Chocolate bar has the form of a rectangle divided into n×m portions.
    Chocolate bar can be split into two rectangular parts
    by breaking it along a selected straight line on its pattern.
    Determine whether it is possible to split it so that one of the parts will have exactly k squares.

    The program reads three integers: n, m, and k.
    It should print YES or NO.
"""

print("""
    For given m x n chockolate bar determines if it is possible 
    to obtain k-square piece by one break (along the whole bar).  
""")

n = int(input("number of chockolate rows: "))
m = int(input("number of chockolate columns: "))
k = int(input("number of squares to be splitted off in one break: "))

condition_0 = k <= n * m and k > 0
m_div = k % m == 0
n_div = k % n == 0

if condition_0 and (m_div or n_div):
    print('YES')
else:
    print('No')
