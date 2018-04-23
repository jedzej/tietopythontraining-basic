#1.
#Write a function named collatz() that has one parameter named number. If number is even, then collatz() should print number // 2 and return this value. If number is odd, then collatz() should print and return 3 * number + 1.

#2.
#Then write a program that lets the user type in an integer and that keeps calling collatz() on that number until the function returns the value 1. (Amazingly enough, this sequence actually works for any integer—sooner or later, using this sequence, you’ll arrive at 1! Even mathematicians aren’t sure why. Your program is exploring what’s called the Collatz sequence, sometimes called “the simplest impossible math problem.”)

#1.
def collatz(number):
    ret = 0
    if (number%2 == 0):
        ret = number // 2
    else:
        ret = 3* number + 1

    print(ret)
    return ret

print("Enter the number:")
n = int(input())
collatz(n)

#2.

def collatz_1(num):
    res = collatz(num)
    if res == 1:
        return 1
    else:      
        return collatz_1(res)

print("Enter the number:")
n = int(input())
collatz_1(n)
    
