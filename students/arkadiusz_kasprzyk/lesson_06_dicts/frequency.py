# frequency.py

N = int(input("Give number of lines to read: "))

dic = dict()

for n in range(N):
    line = input("line {}: ".format(n + 1)).split()
    for word in line:
        dic.setdefault(word, 0)
        dic[word] += 1

print("")  # just aestethics for testing in Snakify

ll = list(zip(dic.values(), dic.keys()))
ll.sort(key=lambda x: (-x[0], x[1]))
for tupl in ll:
    print("{} : {}".format(tupl[1], tupl[0]))
