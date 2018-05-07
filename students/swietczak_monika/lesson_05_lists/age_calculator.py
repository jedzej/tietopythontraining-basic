int_list = [int(s) for s in input(
    "Enter a list of ages, each number should be followed by comma: ").split(
    ",")]
# print(int_list)
avg_children = 0
avg_adult = 0
try:
    adult_list = [val for val in int_list if val >= 18]
    if len(adult_list) > 0:
        avg_adult = sum(adult_list) / len(adult_list)
    children_list = [val for val in int_list if val < 18]
    if len(children_list) > 0:
        avg_children = sum(children_list) / len(children_list)
except ValueError:
    print("Incorrect data")

print("Average adult age= ", avg_adult)
print("Average children age = ", avg_children)
