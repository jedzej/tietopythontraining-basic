from collections import defaultdict

list_to_check = defaultdict(int)


def counter():
    lines = int(input("How many lines you want to have? "))
    while lines > 0:
        line_with_words = str(input("Type the line: ")).lower().split()
        lines -= 1
        for word in line_with_words:
            list_to_check[word] += 1

counter()
sorted_decreasing = sorted(list_to_check.items(), key=lambda t: t[1], reverse=True)
print(sorted_decreasing)
