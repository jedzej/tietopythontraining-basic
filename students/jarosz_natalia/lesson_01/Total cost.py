
dollar = int(input())
cents = int(input())
n = int(input())
costD = dollar * n
costCd = (cents * n // 100)
costC = cents *n % 100
print(str(costD + costCd) + " " + str(costC) )