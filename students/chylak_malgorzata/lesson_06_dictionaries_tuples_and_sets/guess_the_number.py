n = int(input())
guess = set(range(1, n + 1))

while True:
    number = input()
    if number not in ("YES", "NO", "HELP"):
        a = set(int(s) for s in number.split())
    if number == "YES":
        guess &= a
    if number == "NO":
        guess -= a
    elif number == "HELP":
        break

for elem in guess:
    print("".join(str(elem)))
