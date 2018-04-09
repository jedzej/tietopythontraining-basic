# script to print a ladder of n steps given an integer <= 9
print("enter a number")
number = int(input())
for i in range(number+1):
    for k in range(0,i):
        print(k+1, end='')
    print()
