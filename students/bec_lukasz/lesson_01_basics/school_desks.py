# Read an integer:
# a = int(input())
# Print a value:
# print(a)

studentsA=int(input())
studentsB=int(input())
studentsC=int(input())

desksA = studentsA//2+studentsA%2
desksB = studentsB//2+studentsB%2
desksC = studentsC//2+studentsC%2

print(desksA+desksB+desksC)