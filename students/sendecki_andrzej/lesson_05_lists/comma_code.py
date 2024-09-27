#Say you have a list value like this:
#spam = ['apples', 'bananas', 'tofu', 'cats']
#Write a function that takes a list value as an argument and returns a string with all the items
#separated by a comma and a space, with "and" inserted before the last item.
#For example, passing the previous spam list to the function would return 'apples, bananas,
# tofu, and cats'. But your function should be able to work with any list value passed to it.

def show_list(my_list):

    my_string=''
    for i in range(len(my_list) - 2):
        my_string = my_string + my_list[i] + ", "

    my_string = my_string + my_list[-2] + " and " + my_list[-1]
    
    return my_string

spam = ['apples', 'bananas', 'tofu', 'cats', 'dogs', 'hamsters']
print(show_list(spam))

