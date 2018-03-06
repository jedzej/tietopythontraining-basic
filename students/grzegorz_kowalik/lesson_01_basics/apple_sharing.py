n = int(input("Students: "))
k = int(input("Apples: "))

print("Each student will get " + str(k//n) + " apples")
print("There will be " + str(k % n) + " apples left")