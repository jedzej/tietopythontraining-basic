students = int(input("Students: "))
apples = int(input("Apples: "))

print("Each student will get " + str(apples // students) + " apples")
print("There will be " + str(apples % students) + " apples left")
