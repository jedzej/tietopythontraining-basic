# https://snakify.org/lessons/if_then_else_conditions/problems/chocolate/
# piotrsta

edgeN = int(input())
edgeM = int(input())
squares = int(input())
if (squares % edgeM == 0 or squares % edgeN == 0) and edgeN * edgeM >= squares:
    print('YES')
else:
    print('NO')
