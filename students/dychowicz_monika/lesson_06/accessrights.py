def check_rights():
    n = int(input("Enter number of files: "))
    rights = {}
    for i in range(n):
        f_line = input("Enter file name and allowed\
 operations separated by space (R/W/X): ").split()
        rights[f_line[0]] = set(f_line[1:])
    m = int(input("Enter number of operations: "))
    for i in range(m):
        action = input(
            "Enter operation and affected file\
 (e.g. \"read file.txt\"): ").split()
        if action[0] == "write":
            action[0] = "W"
        elif action[0] == "read":
            action[0] = "R"
        elif action[0] == "execute":
            action[0] = "X"
        if action[0] in rights[action[1]]:
            print("OK")
        else:
            print("Access denied")


if __name__ == "__main__":
    check_rights()