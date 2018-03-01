import math

firstClass = int(input("Write how many students are in first class: "))
secondClass = int(input("Write how many students are in second class: "))
thirdClass = int(input("Write how many students are in third class: "))

desksInFirstClass = math.ceil(firstClass/2)
desksInSecondClass = math.ceil(secondClass/2)
desksInThirdClass = math.ceil(thirdClass/2)

totalDesks = desksInFirstClass + desksInSecondClass + desksInThirdClass

print("Total number of desks: " + str(totalDesks))
