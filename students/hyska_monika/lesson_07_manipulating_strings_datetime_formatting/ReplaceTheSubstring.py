# function replace 1  by word one


def replace_number_to_string(text, number, text_number):
    text = text.replace(number, text_number)
    print(text)
    return text


my_string = 'AniAla1'
my_string2 = 'Ani5Ala'
my_string3 = 'A1a1a1'
my_string4 = '1+1=2'
my_string5 = 'Hello, 2345678990'
my_string6 = '1111111111111111111111111111111111'

replace_number_to_string(my_string, '1', 'one')
replace_number_to_string(my_string2, '5', 'five')
replace_number_to_string(my_string3, '1', 'one')
replace_number_to_string(my_string4, '1', 'one')
replace_number_to_string(my_string5, '1', 'one')
replace_number_to_string(my_string6, '1', 'one')
