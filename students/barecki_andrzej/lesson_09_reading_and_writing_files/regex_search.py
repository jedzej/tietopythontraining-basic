import os
import re

user_regex = re.compile(r'{}'.format(input("Set regex definition:")))
for elem in os.listdir(os.getcwd()):
    if elem.lower().endswith('.txt'):
        input_file = open(elem, "r")
        content = input_file.readlines()
        for line in content:
            if user_regex.match(line):
                print("Content: {0} in file {1}".format(line, elem))
