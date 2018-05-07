# function to check that file has access rights
from functions_lesson06 import list_elements_str, change_to_dict


def access_rights(inventory):
    rights = {'read': 'r', 'write': 'w', 'execute': 'x'}
    n = int((input('How many access rights do you want check?:')))
    for i in range(n):
        command = str((input("put command:")))
        command = command.split(' ')
        try:
            right = command[0]
            right = rights[right]
            file_name = command[1]
            file_rights = inventory[file_name]
            if right in file_rights:
                print("OK")
            else:
                print("Access denied")
        except KeyError:
            print('There is no command or file.')


print("For size list put how many files do you have."
      "\nFor one element of list put file name and access rights,"
      " separate using space."
      "\nEg. kot.j x w r")
access_rights(change_to_dict(list_elements_str()))
#inventory = {'kot.j' : ['r', 'w',  'x'],
#             'pies.l' : ['r'], 'mysz' : ['r', 'x']}
# access_rights(inventory)
