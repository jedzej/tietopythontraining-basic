max_index = [0, 0]
m, n = [int(s) for s in
        input("Enter two numbers with a space between them ").split()]
a = [[int(j) for j in
      input("Enter values in a row number " + str(i) + ": ").split()] for i in
     range(m)]

max_number = a[0][0]
for i in range(m):
    if max(a[i]) > max_number:
        max_number = max(a[i])
        max_index[0] = i
        max_index[1] = a[i].index(max_number)

print("Index of maximum number: ", max_index[0], max_index[1])
