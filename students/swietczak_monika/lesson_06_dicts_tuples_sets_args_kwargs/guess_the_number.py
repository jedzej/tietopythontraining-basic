n = int(input())
possible_numbers = set(range(1, n + 1))

while True:
    val = input()
    if val not in ("YES", "NO", "HELP"):
        a = set(int(s) for s in val.split())
    if val == "YES":
        possible_numbers &= a
    if val == "NO":
        possible_numbers -= a
    elif val == "HELP":
        break

for elem in possible_numbers:
    print("".join(str(elem)))
