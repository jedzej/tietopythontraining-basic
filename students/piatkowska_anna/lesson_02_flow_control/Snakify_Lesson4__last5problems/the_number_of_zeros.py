#Statement
#Given N numbers: the first number in the input is N, after that N integers are given. 
#Count the number of zeros among the given integers and print it.
#You need to count the number of numbers that are equal to zero, 
#not the number of zero digits.

def TheNumberOfZeros():
    print("Enter number of integers that will be processed:")
    a = int(input())
    zerosCount = 0
    print("Enter "+ str(a) + " numbers:")
    for i in range(a):
        print("Number " + str(i+1) +":")
        b = int(input())
        if (b==0):
            zerosCount += 1
    print("Count of numbers that are equal to zero:")
    print (zerosCount)

if __name__ == '__main__':
    TheNumberOfZeros()