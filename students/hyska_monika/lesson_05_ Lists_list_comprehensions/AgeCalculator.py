# Function print age average for adults and child number
from create_lists import list_elements


def check_age(mylist):
    adults_list = [mylist[x] for x in range(len(mylist)) if mylist[x] >= 18]
    if len(adults_list) > 0:
        average_adults = sum(adults_list) / len(adults_list)
    else:
        average_adults = "Missing adults."
    print("Average of adults: ", average_adults)
    child_list = [mylist[x] for x in range(len(mylist)) if mylist[x] < 18]
    count_child = len(child_list)
    print("Number of child: ", count_child)


print("Put data for list: number of people, and age for these people.")
check_age(list_elements())
