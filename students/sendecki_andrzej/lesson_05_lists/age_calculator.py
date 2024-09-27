#Age calculator - write a program that for given list of people's ages calculate the average age of adults (age >= 18) and count the children (age < 18). Use list comprehensions.

def avg(list):
    a = 0
    for i in range(len(list)):
        a = a + list[i]

    return a/len(list)


print("People:")
ages_list = [2, 4, 4, 19, 57, 3, 11, 72, 32 , 8, 18, 1, 9]
print(ages_list)

adults_list = [age for age in ages_list if age >= 18]
print("Adults:")
print(adults_list)

children_list = [age for age in ages_list if age < 18]
print("Children:")
print(children_list)

print("Average adults' age:")
print(avg(adults_list))

print("Number of children:")
print(len(children_list))
