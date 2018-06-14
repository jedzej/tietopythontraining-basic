text_set = set()

print("Enter the number of lines in the text:")
n = int(input())
for i in range(n):
    print("Enter line " + str(i+1) + " of the text:")
    tmp_set = input().split(" ")
    text_set.update(tmp_set)

print(len(text_set))
