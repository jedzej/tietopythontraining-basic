print('Give hours 0 ≤ H < 12:')
H = int(input())

print('Give minutes 0 ≤ M < 60:')
M = int(input())

print('Give seconds 0 ≤ S < 60:')
S = int(input())

sum = H + M/60 + S/3600
degrees = 90*sum/3

print(str(H) + ':' + str(M) + ':' + str(S) + ' = ' + str(degrees) + '[degrees]')