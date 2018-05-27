n = int(input())
files_dict = dict()
OPERATIONS_DICT = {"read": "R", "write": "W", "execute": "X"}

for i in range(n):
    rights = ""
    file_rights = input().split()
    file = file_rights[0]
    for val in file_rights[1:]:
        rights += val
    files_dict[file] = rights

m = int(input())
for _ in range(m):
    operation, file = input().split()
    if OPERATIONS_DICT[operation] in files_dict[file]:
        print("OK")
    else:
        print("Access denied")
