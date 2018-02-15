import os

PROCESS_CAR_DATA = True

if os.path.exists('data.csv'):
    print('Processing data.csv file')
    with open('data.csv') as f:
        a = []
        total = 0
        for l in f:
            a.append(l.split(',')[2])

    for s in a:
        total += int(s)

    print('Avgerage age is', total/len(a))

    if PROCESS_CAR_DATA == True:
        with open('data.csv') as f:
            z = 0
            for l in f:
                if l.split(',')[3][:-1] == 'true':
                    z += 1

        print('Citzens with car ', z)
else:
    print('No data.csv file')


