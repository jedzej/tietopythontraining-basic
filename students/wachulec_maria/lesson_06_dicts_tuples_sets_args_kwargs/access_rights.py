def access_rights():
    operations = {'write': 'W', 'read': 'R', 'execute': 'X'}
    files = {}
    for i in range(int(input())):
        filesystem = input().split()
        files[filesystem[0]] = filesystem[1:]
    for j in range(int(input())):
        request_operation, request_file = input().split()
        if operations[request_operation] in files[request_file]:
            print('OK')
        else:
            print("Access denied")


access_rights()
