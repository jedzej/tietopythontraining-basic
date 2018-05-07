avg = 0
ages = []
people = int(input("Enter the number of people: "))

for x in range(people):
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

print("Average adult age: {:s}".format(str(avg)))
print("Kids counter: {:s}".format(str(len(kids))))
