# A car can cover distance of N kilometers per day. How many days will it take to cover a route of length M kilometers? The program gets two numbers: N and M.

# Read an integer:
N = int(input())
M = int(input())
# Print a value:
if(M%N == 0):
    print(M // N)
else:
    print((M // N)+1)
