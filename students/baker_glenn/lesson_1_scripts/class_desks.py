# script to calcualte the smallest amount of desks to be purchased
import math

print("enter the number of students in class a")
class_a = int(input())
print("enter the number of students in class b")
class_b = int(input())
print("enter the number of students in class c")
class_c = int(input())
print("the number of desks required is " + str((math.ceil(class_a / 2) + math.ceil(class_b / 2) + math.ceil(class_c / 2))))
