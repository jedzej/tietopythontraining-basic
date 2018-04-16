a = input('Enter array dimensions: ').split()

for i in range(int(a[0])):
    for j in range(int(a[1])):
        if i % 2 == 0:
            if j % 2 == 0:
                print('. ', end='')
            else:
                print('* ', end='')

        else:
            if j % 2 == 0:
                print('* ', end='')
            else:
                print('. ', end='')
    print()
