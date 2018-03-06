# Read an integers; A dollars, B cents, N cakes:
A = int(input())
B = int(input())
N = int(input())
dolars=(A+B/100)*N
# Print how many dollars and cents should one pay for N cupcakes:
print(str(int(dolars)) + ' ' + str(int(dolars*100)%100))