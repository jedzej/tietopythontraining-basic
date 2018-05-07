number_of_files = int(input())
file_access_rights = dict()

for file in range(number_of_files):
    entry = input().split(' ')
    file_access_rights[entry[0]] = entry[1:]

number_of_operations = int(input())
for operation in range(number_of_operations):
    access_denied = True
    operation_entry = input().split(' ')
    if operation_entry[0] == "read":
        operation_entry[0] = "R"
    elif operation_entry[0] == "write":
        operation_entry[0] = "W"
    elif operation_entry[0] == "execute":
        operation_entry[0] = "X"

    if operation_entry[1] in file_access_rights:
        for allowed_access in file_access_rights[operation_entry[1]]:
            if operation_entry[0] == allowed_access:
                access_denied = False
                break
    if access_denied:
        print("access denied")
    else:
        print("OK")
