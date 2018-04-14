avg = 0
ages = []
peoples = int(input("How many people? "))
for x in range(peoples):
    print("Person number", x + 1, "age: ")
    ages.append(int(input()))

adults = [x for x in ages if x >= 18]
kids = [x for x in ages if x < 18]
if adults == []:
    print("No adults")
else:
    for i in adults:
        avg += i
    avg /= len(adults)

print("Average adult age: " + str(avg))
print("Kids counter: " + str(len(kids)))
