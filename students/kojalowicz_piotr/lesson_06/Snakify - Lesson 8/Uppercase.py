def capitalize(lower_case_word):
    new_capitalize_string = lower_case_word.split()
    output = ''
    for word in new_capitalize_string:
        output += word.capitalize() + " "
    return output

print(capitalize(input()))
