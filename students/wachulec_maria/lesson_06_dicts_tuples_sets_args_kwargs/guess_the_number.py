from random import randint


n = int(input())
secret_number = randint(1, n)
set_of_results = set(range(1, n + 1))
print(set_of_results)
while True:
    guess = input()
    if guess == "HELP":
        break
    else:
        guess = set(int(s) for s in guess.split())
    if secret_number in guess:
        print("YES")
        set_of_results &= guess
    else:
        print("NO")
        set_of_results ^= guess
    print(set_of_results)
