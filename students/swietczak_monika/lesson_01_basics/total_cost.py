# Read an integer:
a = int(input())
b= int(input())
n=int(input())
# Print a value:
# print(a)
sum_of_dollars=a*n+(b*n)//100
sum_of_cents=(b*n)%100
print(str(sum_of_dollars)+" "+str(sum_of_cents))