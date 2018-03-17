print("Apple sharing\n")

N = int(input("Enter the number of students: "))
K = int(input("Enter the number of apples: "))

a = K // N
b = K % N

print("\nEach student will get %d apples" %a)
print("The number of apples in the basket:", b)