import math
classA = int(input("Number of students in class A: "))
classB = int(input("Number of students in class B: "))
classC = int(input("Number of students in class C: "))

print(math.ceil(classA / 2) + math.ceil(classB / 2) + math.ceil(classC / 2))
