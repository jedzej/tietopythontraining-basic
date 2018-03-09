# Read an integer:
a = int(input())
b = int(input())
n = int(input())
# Print a value:
print(str((int(float(b/100)*n + a*n))) + ' ' + str(round(((float(b/100)*n + a*n)-int(float(b/100)*n + a*n))*100)))
