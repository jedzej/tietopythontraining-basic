# Read an integer:
A = int(input())
B = int(input())
N = int(input())
# Print a value:
total = (A + B/100)*N
print(str(int(total)) + " " + str(round(float(total * 100) - (int(total)*100))))