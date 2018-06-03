word_keys = ["ADJECTIVE", "NOUN", "ADVERB", "VERB"]

input_user_file = open('user_input_text_file.txt', 'r')
user_content = input_user_file.read()
input_user_file.close()

for elem in word_keys:
    while elem in user_content:
        print("Enter an {0}:".format(elem.lower()))
        user_content = user_content.replace(elem, input(), 1)

output_user_file = open('user_output_text_file.txt', 'w')
output_user_file.write(user_content)
output_user_file.close()
