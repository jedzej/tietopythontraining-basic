people_age = [int(i) for i in input("Type age of people: ").split()]

number_of_children = 0
average_age = []

for person in people_age:
    if person < 18:
        number_of_children += 1
    else:
        average_age.append(person)

print("The number of children is: " + str(number_of_children))
print("The average adult age is: " + str(sum(average_age)/len(average_age)))


