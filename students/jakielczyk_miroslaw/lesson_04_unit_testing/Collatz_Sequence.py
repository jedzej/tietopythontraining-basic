# Collatz Sequence

def main():
    print ("Enter the number ")
    number = int(input())
    result = number
    while result != 1:
        result = collatz(result)
        print (result)
   
def collatz(number):
    if number % 2 == 0:
        return (number // 2)
    elif number % 2 == 1:
        return (3 * number + 1)

if __name__ == "__main__":
    main()
        
        
