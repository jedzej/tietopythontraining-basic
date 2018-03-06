# script to calculate the amount of apples to be dispributed evenly among students and the remained
print("enter the number of students")
students = int(input())
print("enter amount of apples")
apples = int(input())
print("each student gets " + str((apples // students)) + ", there are " + str((apples % students)) + " remaining in the basket")
