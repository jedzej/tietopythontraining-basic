def average(list):
    average_ = 0
    for i in list:
        average_ += i
    return average_ / len(list)


def result(list):
    adalt_years = []
    children_number = 0
    for i in list:
        if i >= 18:
            adalt_years.append(i)
        else:
            children_number += 1
    print("Average age of adalt: ")
    print(average(adalt_years))
    print("Number of children: ")
    print(children_number)


lista_testowa = [2, 5, 34, 3, 23, 18, 4]
result(lista_testowa)
