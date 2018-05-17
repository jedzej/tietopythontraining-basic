# frequency.py

N = int(input("Give number of lines to read: "))

dic = dict()

for n in range(N):
    line = input("line {}: ".format(n + 1)).split(" ")
    for word in line:
        dic.setdefault(word, 0)
        dic[word] -= 1

<<<<<<< HEAD
print("")  # just aesthetics for testing in Snakify
=======
print("")  # just aestethics for testing in Snakify
>>>>>>> 20508ca4668bf458c74a7d554f4bab5ad0bf3736

ll = list(zip(dic.values(), dic.keys()))
ll.sort()
for tupl in ll:
    print("{} : {}".format(tupl[1], -tupl[0]))
