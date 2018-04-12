spam_list = input().split(' ')
count = 0
for x in range(1, len(spam_list) - 1):
    if (int(spam_list[x]) - int(spam_list[x - 1])) > 0 \
            and (int(spam_list[x]) - int(spam_list[x + 1])) > 0:
        count += 1
print(count)
