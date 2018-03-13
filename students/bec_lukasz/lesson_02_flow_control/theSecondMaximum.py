# Read an integer:
# a = int(input())
# Print a value:
# print(a)

greatest = 2
second = 1
temporary = 0
element = int(input())
while element != 0:
    if(element>greatest):
        temporary = greatest
        greatest = element
        second = temporary
    elif(element>second and element<greatest):
       second = element
    element = int(input())
    
print(second)