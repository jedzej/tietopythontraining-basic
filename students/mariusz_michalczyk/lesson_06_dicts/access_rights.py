def get_full_name_rights(rights):
    full = set()
    for right in rights:
        if right == "R":
            full.add("read")
        if right == "W":
            full.add("write")
        if right == "X":
            full.add("execute")
    return full


def get_files_permissions(n):
    files_rights_map = {}
    for i in range(n):
        line = [s for s in input().split()]
        file_name = line[0]
        rights = set(line[1::])
        files_rights_map[file_name] = get_full_name_rights(rights)
    return files_rights_map


def check_access(m, permissions):
    for i in range(m):
        line = [s for s in input().split()]
        operation = line[0]
        file_name = line[1]
        if operation in permissions[file_name]:
            print("OK")
        else:
            print("Access Denied")


if __name__ == '__main__':
    n = int(input())
    permissions = get_files_permissions(n)
    m = int(input())
    check_access(m, permissions)
