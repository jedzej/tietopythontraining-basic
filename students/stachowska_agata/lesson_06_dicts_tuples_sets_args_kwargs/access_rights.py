operations = {'read': 'R', 'write': 'W', 'execute': 'X'}
files = {}

for i in range(int(input())):
    name, *rights = input().split()
    files[name] = rights


for test in range(int(input())):
    operation, name = (i for i in input().split(' '))
    if operations.get(operation) in files.get(name):
        print('OK')
    else:
        print('Access denied')
