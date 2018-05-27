def input_files():
    number_of_file = \
        int(input("the number of files contained in the filesystem: "))
    new_file = {}
    new_file["X"] = []
    new_file["R"] = []
    new_file["W"] = []
    for i in range(number_of_file):
        file_and_operations = input('file name and allowed operations: ')
        file_and_operations = file_and_operations.split(' ')
        if "X" in file_and_operations:
            new_file["X"].append(file_and_operations[0])
        if "R" in file_and_operations:
            new_file["R"].append(file_and_operations[0])
        if "W" in file_and_operations:
            new_file["W"].append(file_and_operations[0])
    return new_file


def input_request():
    number_of_requested = int(input('the number of requested files: '))
    new_file = []
    for i in range(number_of_requested):
        requested = input('the requested operation on file and its name: ')
        requested = requested.split(' ')
        new_file.append(requested)
    return new_file


def result(a, b):
    file_operation = 0
    file_permision = 1
    for i in b:
        if i[file_operation] == "write":
            if i[file_permision] in a["W"]:
                print("OK")
            else:
                print("Access denied")
        if i[file_operation] == "read":
            if i[file_permision] in a["R"]:
                print("OK")
            else:
                print("Access denied")
        if i[file_operation] == "execute":
            if i[file_permision] in a["X"]:
                print("OK")
            else:
                print("Access denied")


a = input_files()
b = input_request()
result(a, b)
