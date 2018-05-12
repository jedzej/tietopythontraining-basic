age_list = map(int, input().split())

childrens = []
adults = []

for age in age_list:
    if age > 18:
        adults.append(age)
    else:
        childrens.append(age)

adults_mean_age = 0
childrens_mean_age = 0
for adult in adults:
    adults_mean_age = adults_mean_age + adult
for children in childrens:
    childrens_mean_age = childrens_mean_age + children


if len(adults) > 0:
    adults_mean_age = adults_mean_age / len(adults)
if len(childrens) > 0:
    childrens_mean_age = childrens_mean_age / len(childrens)

print("Adults average age is ", adults_mean_age)
print("Childrens average age is ", childrens_mean_age)
