n = 0
while (n < 1):
    n = int(input("Enter amount of students: "))
    print ("Enter at least one student")

k = int(input("Enter amount of apples: "))
print("Every student will get: " + str(k // n) + " apples")
print("Remained apples: " + str(k % n) + " apples")
