print("Enter number of students (n)")
n = int(input())

print("Enter number of apples (k)")
k = int(input())

apples_got = k // n
apples_remaining = k % n

print("Each student will get " + str(apples_got) + " apples.")
print(str(apples_remaining) + " apples will remain in the basket.")