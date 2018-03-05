print("1.1 «Sum of three numbers»")
a = int(input())
b = int(input())
c = int(input())
print(a + b + c)

print("1.2 «Area of right-angled triangle»")
b = int(input())
h = int(input())
print (0.5 * h * b)

print("1.3 «Hello, Harry!»")
a = (input())
print("Hello, " + a + "!")

print("1.4 «Apple sharing»")
# Read the numbers like this:
n = int(input())
k = int(input())

# Print the result with print()
print(k//n)
print(k%n)

print("1.5 «Previous and next»")
# Read an integer:
a = int(input())
# Print a value:
print("The next number for the number", a, "is", str(a+1) + ".")
print("The previous number for the number", a, "is", str(a-1) + ".")

print("1.6 «School desks»")
# Read an integer:
a = int(input())
b = int(input())
c = int(input())
desks = a//2 + a%2 + b//2 + b%2 + c//2 + c%2
# Print a value:
print(desks)

print("2.1 «Last digit of integer»")
# Read an integer:
a = int(input())
# Print a value:
print(str(a)[-1])

print("2.2 «Tens digit»")
# Read an integer:
a = int(input())
# Print a value:
print((a%100-a%10)//10)

print("2.3 «Sum of digits»")
# Read an integer:
a = int(input())
# Print a value:
print((a%1000//100)+(a%100//10)+(a%10))

print("2.4 «Fractional part»")
# Read an integer:
a = float(input())
# Print a value:
print(str(a-int(a)))

print("2.5 «First digit after decimal point»")
# Read an integer:
a = float(input())
# Print a value:
print(str(a-int(a))[2])

print("2.6 «Car route»")
import math
# Read an integer:
N = int(input())
M = int(input())
# Print a value:
print(math.ceil(M/N))

print("2.7 «Digital clock»")
# Read an integer:
N = int(input())
# Print a value:
print(N//60, N%60)

print("2.8 «Total cost»")
# Read an integer:
A = int(input())
B = int(input())
N = int(input())
# Print a value:
print(A*N+(B*N)//100, (B*N)%100)



print("2.9 «Clock face - 1»")
# Read an integer:
H = int(input())
M = int(input())
S = int(input())

# Print a value:
print(H*360/12 + M*360/60/12 + S*360/60/60/12)
