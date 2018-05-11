'''
Statement
The virus attacked the filesystem of the supercomputer and broke the control
of access rights to the files. For each file there is a known
set of operations which may be applied to it:
write W,
read R,
execute X.
The first line contains the number N — the number of files contained
in the filesystem. The following N lines contain the file names and allowed
operations with them, separated by spaces. The next line contains an integer
M — the number of operations to the files. In the last M lines specify the
operations that are requested for files. One file can be requested
many times.

You need to recover the control over the access rights to the files.
For each request your program should return OK if the requested
operation is valid or Access denied if the operation is invalid.
'''


def check_rights():
    n = int(input("Enter number of files: "))
    rights = {}
    for i in range(n):
        f_line = input("Enter file name and allowed\
 oparations separated by space (R/W/X): ").split()
        rights[f_line[0]] = set(f_line[1:])
    m = int(input("Enter number of operations: "))
    for i in range(m):
        action = input(
            "Enter oparation and affected file\
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
