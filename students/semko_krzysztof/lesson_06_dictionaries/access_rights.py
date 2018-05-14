"""
The virus attacked the filesystem of the supercomputer
and broke the control of access rights to the files.
For each file there is a known set of operations which may
 be applied to it:

    write W,
    read R,
    execute X.

The first line contains the number N — the number of files
contained in the filesystem. The following N lines contain
the file names and allowed operations with them, separated
by spaces. The next line contains an integer M — the number
of operations to the files. In the last M lines specify the
operations that are requested for files. One file can be
requested many times.

You need to recover the control over the access rights to
the files. For each request your program should return OK
if the requested operation is valid or Access denied if
the operation is invalid.
"""


def main():
    access_rights = {"R": "read", "W": "write", "X": "execute"}
    files = dict()
    files_num = int(input())
    for i in range(files_num):
        file_name, *access = input().split()
        values = []
        for j in access:
            values.append(access_rights.get(j))
        files[file_name] = values

    operations_num = int(input())
    for i in range(operations_num):
        line = input().split()
        if line[0] in files.get(line[1]):
            print("OK")
        else:
            print("Access Denied")


if __name__ == '__main__':
    main()
