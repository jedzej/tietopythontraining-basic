last_number = int(input())
correct_set = set()
wrong_set = set()
for i in range(0, last_number):
    alice_sentence = input()
    if alice_sentence == "HELP":
        break
    guess = set(alice_sentence.split())
    bob_sentence = input()
    if bob_sentence == "YES":
        if correct_set:
            correct_set = correct_set.intersection(guess)
        else:
            correct_set = guess
    else:
        wrong_set.update(guess)
if correct_set:
    for element in sorted(correct_set.difference(wrong_set)):
        print(element, " ")
else:
    for i in range(1, last_number + 1):
        if i not in wrong_set:
            print(i, " ")
