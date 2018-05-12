def comma_code(list):
    if len(list) == 0:
        print("List is empty")
    elif len(list) == 1:
        print(list[0])
    else:
        print(", ".join(list[0:-1]) + " and " + list[-1])


print("Enter a list separated by space: ")
input_list = [str(x) for x in input().split()]
print(comma_code(input_list))
