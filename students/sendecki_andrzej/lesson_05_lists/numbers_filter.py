#Numbers filter - using list comprehensions write a function that casts list of strings to list of integers and filters numbers within supplied range. Example data:
#
#list_of_strings = ['2', '0', '8', '3']	
#to_filter_range = range(3)	
#[Andrzej] - I believe there is an error below, should be [2, 0]
#expected_output = [8, 3]

print("Enter the range: ", end='')
to_filter_range = int(input())

print("input list:")
list_of_strings = ['2', '0', '8', '3', '-2', '3', '1']	
print(list_of_strings)

expected_output = [ int(n) for n in list_of_strings 
                    if int(n) in range(to_filter_range) ]
print("expected output:")
print(expected_output)
