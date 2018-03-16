#Statement
#Given an integer n, print the sum 1!+2!+3!+...+n!.
#This problem has a solution with only one loop, 
#so try to discover it. And don't use the math library :)

def Addingfactorials():
    print("For given an integer n, the program will print the sum 1!+2!+3!+...+n!.")
    print("Enter a number n:")
    a = int(input())
    sumOfFactorial = 0;
    factorial = 1;
    for i in range(1, a+1):
        factorial = factorial * i
        sumOfFactorial += factorial;
    print("The sum 1!+2!+3!+...+n! is:")
    print(sumOfFactorial)

if __name__ == '__main__':
    Addingfactorials()