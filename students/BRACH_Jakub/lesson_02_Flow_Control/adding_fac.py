n = int(input())
c = 0
master_summ = 0
factorial = 1
for c in range(1,n+1):
   factorial = factorial * c
   master_summ = master_summ + factorial
print(master_summ)
