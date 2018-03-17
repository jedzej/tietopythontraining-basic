# This program returns:
# How many apples will each single student get?
# How many apples will remain in the basket?

n = int(input("Numbers of students: "))
k =  int(input("Numbers of apples: "))

n_apples_s = k // n #numbers apples for 1 student
n_apples_b = k % n #numbers apples left on basket

print("Each student will receive", n_apples_s, "apples.")
print("In basket will stay", n_apples_b, "apples.")