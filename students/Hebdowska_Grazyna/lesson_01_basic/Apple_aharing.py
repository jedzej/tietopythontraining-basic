n_students = int (input("Give students number: "))
k_appels = int (input ("Give apple number: "))

student_appels = int(k_appels/n_students)
basket_appels = k_appels - (n_students * student_appels)

print (student_appels)
print(basket_appels)
