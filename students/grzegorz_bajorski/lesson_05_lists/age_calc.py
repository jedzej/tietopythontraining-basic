people_list = [int(i) for i in input().split()]

adult_age_sum = adult_num = avg_adult_age = 0
kid_num = 0

for i in range (len(people_list)):
	if people_list[i] >= 18:
		adult_age_sum += people_list[i]
		adult_num += 1
	elif people_list[i] < 18:
		kid_num += 1

if adult_num > 0:
	avg_adult_age = adult_age_sum/adult_num

print("Avarage adult age is ", avg_adult_age, " Number of kids: ", kid_num)
