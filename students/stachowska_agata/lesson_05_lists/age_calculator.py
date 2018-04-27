def age_calculate(age):
    average = "There are no adults in the list."
    amount_of_children = [i for i in age if i in range(1, 18)]
    amount_of_adults = [i for i in age if i not in range(18)]
    if len(amount_of_adults) > 0:
        average = sum(amount_of_adults) / len(amount_of_adults)
    return average, len(amount_of_children)


age = [int(i) for i in input().split()]
adults, children = age_calculate(age)

print("Number of children: " + str(children))
if type(adults) != str:
    print("Average age of adults: " + str(adults))
else:
    print(adults)
