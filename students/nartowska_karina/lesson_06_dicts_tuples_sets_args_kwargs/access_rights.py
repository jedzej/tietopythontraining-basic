def main():
    print("Result:")
    set_of_operations = {
        'write': 'W',
        'read': 'R',
        'execute': 'X',
    }
    files = {}
    for i in range(int(input())):
        file_name, *allowed_operations = input().split()
        files[file_name] = set(allowed_operations)

    for i in range(int(input())):
        requested_operation, file_name = input().split()
        if set_of_operations[requested_operation] in files[file_name]:
            print("OK")
        else:
            print("Access denied")


if __name__ == '__main__':
    main()
