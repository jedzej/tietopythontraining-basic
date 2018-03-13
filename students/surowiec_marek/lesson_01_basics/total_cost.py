# Read A dollars, B cents, N cakes:
A = int(input())
B = int(input())
N = int(input())
dollars_with_cents = (A + B/100) * N
# Print how many dollars and cents should one pay for N cupcakes:
print(str(int(dollars_with_cents)) + ' ' + str(int(dollars_with_cents*100)%100))
