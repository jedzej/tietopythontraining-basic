# Program print how many time appears 0

N = int(input("How many numbers do you want put?:"))
count = 0

for i in range(1, N + 1):
    print("Please set", i, "number:")
    n = int(input())
    if n == 0:
        count += 1

print("0 appears", count, "times.")
