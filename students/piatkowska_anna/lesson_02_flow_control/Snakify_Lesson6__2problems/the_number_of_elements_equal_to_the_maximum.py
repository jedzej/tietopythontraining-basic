#Statement
#A sequence consists of integer numbers and ends with the number 0. 
#Determine how many elements of this sequence are equal to its largest element.

def CountMaxElements():
    print("Enter integer number (0 to end processing):")
    max = int(input())
    a = max
    maxCount = 1
    while(a != 0):
        print("Enter integer number (0 to end processing):")
        a = int(input())
        if (a > max):
            max = a
            maxCount = 1
        elif (a == max):
            maxCount += 1
    print("The count of elements of this sequence that are equal to its largest element is:")
    print(maxCount)

if __name__ == '__main__':
    CountMaxElements()