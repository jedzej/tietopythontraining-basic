# Read the number of dollars (A) and cents (B) the cupcake costs
# and the number of cupcakes (N)
A = int(input())
B = int(input())
N = int(input())
# Print the summarized cost of N cupcakes
print(N*A + N*B//100, N*B % 100)
