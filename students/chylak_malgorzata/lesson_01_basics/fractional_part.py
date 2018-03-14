import math

n = float(input())  # float, because there's a number with a comma
    # print(math.modf(n))
    # print('0.'.join(str(n).split('.')[1]))
frac = n - int(n)
print("%.2f" % frac)
