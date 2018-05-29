def collecting_list_elements():
    a = []
    while True:
        a.append(int(input('Give a list element ')))
    return a


filter_age = 18
list_to_be_filtered = collecting_list_elements()
adults_list = [x for x in list_to_be_filtered if x >= filter_age]
print(sum(adults_list) / len(adults_list))
kids_list = [x for x in list_to_be_filtered if x < filter_age]
print(len(kids_list))
