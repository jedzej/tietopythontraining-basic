# frequency.py

N = int(input("Give number of lines to read: "))

dic = dict()

for n in range(N):
    line = input("line {}: ".format(n + 1)).split(" ")
    for word in line:
        dic.setdefault(word, 0)
        dic[word] -= 1

# dic = {"a" : -3, "b" : -4, "c": -1, "d" : -1, "e" : -2}

ll = list(zip(dic.values(), dic.keys()))
ll.sort()
for tupl in ll:
    print("{} : {}".format(tupl[1], -tupl[0]))
