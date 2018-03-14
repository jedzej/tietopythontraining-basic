# lesson_01_basics
# Total cost
#
# Statement
# A cupcake costs A dollars and B cents. Determine, how many dollars and cents
# should one pay for N cupcakes. A program gets three numbers: A, B, N.
# It should print two numbers: total cost in dollars and cents.

print("Enter cupcake price: dollars")
A = int(input())
print("Enter cupcake price: cents")
B = int(input())
print("Enter number of cupcakes")
N = int(input())

res = N * A + (N * B) / 100

res_dol = int(res)
res_cent = int((res - int(res)) * 100)

print("One should pay " + str(res_dol) + " dollar(s) and " + str(res_cent) + " cent(s).")

