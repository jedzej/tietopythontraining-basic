# Read an integer:
a = int(input())
b = int(input())
n = int(input())
# Print a value:
total = (a + b/100)*n
print(str(int(total)) + " " + str(round(float(total * 100) - (int(total)*100))))
