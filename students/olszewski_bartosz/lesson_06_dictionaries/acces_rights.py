number_of_files = int(input())
file_access_rights = dict()
ACTION = 0
ACTION_2 = 1

for file in range(number_of_files):
    entry = input().split(' ')
    file_access_rights[entry[ACTION]] = entry[ACTION_2:]

number_of_operations = int(input())
for operation in range(number_of_operations):
    access_denied = True
    operation_entry = input().split(' ')
    if operation_entry[ACTION] == "read":
        operation_entry[ACTION] = "R"
    elif operation_entry[ACTION] == "write":
        operation_entry[ACTION] = "W"
    elif operation_entry[ACTION] == "execute":
        operation_entry[ACTION] = "X"

    if operation_entry[ACTION_2] in file_access_rights:
        for allowed_access in file_access_rights[operation_entry[ACTION_2]]:
            if operation_entry[ACTION] == allowed_access:
                access_denied = False
                break
    if access_denied:
        print("Access denied")
    else:
        print("OK")
