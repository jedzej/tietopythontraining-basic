# Read an integer numbers of students in 3 classes:
a = int(input())
b = int(input())
c = int(input())
print('We need ' + str((a//2+a%2)+(b//2+b%2)+(c//2+c%2)) + ' desks in total')
# shorter line:
#print(a//2+a%2+b//2+b%2+c//2+c%2)