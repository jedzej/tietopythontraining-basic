def age_calculator(ll):
    adults = [l for l in ll if l >= 18]
    adults_mean = sum(adults)/len(adults)
    kids = [l for l in ll if l <18]
    kids_number = len(kids)
    return adults_mean, kids_number

#ll = [5,2,1,4]
#sum(ll)/len(ll)

ll = [18, 2, 24, 8, 9]
print(age_calculator(ll))