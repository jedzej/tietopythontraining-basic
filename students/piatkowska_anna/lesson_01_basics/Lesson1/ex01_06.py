#Statement
#A school decided to replace the desks in three classrooms. 
#Each desk sits two students. 
#Given the number of students in each class, print the smallest possible number of desks that can be purchased.
#The program should read three integers: 
#the number of students in each of the three classes, a, b and c respectively.

#In the first test there are three groups.
#The first group has 20 students and thus needs 10 desks. 
#The second group has 21 students, so they can get by with no fewer than 11 desks. 
#11 desks is also enough for the third group of 22 students. 
#So we need 32 desks in total. 

print("Enter number of students in first class:")
a = int(input())
sum = a//2 + a%2
print("Enter number of students in second class:")
b = int(input())
sum += b//2 + b%2
print("Enter number of students in third class:")
c = int(input())
sum += c//2 + c%2
print("The smallest possible number of desks that can be purchased is: " + str(sum))