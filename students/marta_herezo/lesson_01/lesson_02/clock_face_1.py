print('Give hours 0 ≤ H < 12:')
H = int(input())

print('Give minutes 0 ≤ M < 60:')
M = int(input())

print('Give seconds 0 ≤ S < 60:')
S = int(input())

sum = 360/(int(H + (M/60) + (S/3600))

#sum_m = sum_m/60
#print(sum_m)
#sumS = S/3600
#print(sumS)

print('It is: ' + str(sum))