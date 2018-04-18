# program print "." for hit pins and for doesn't hit pins print "I"


pins_number = int((input("How many pins?: ")))
throws_number = int((input("How many throwss?: ")))

pins_list =  ["I" for i in range(pins_number)]
print(pins_list)


for i in range(throws_number):
    print("Put range throws pins: ")
    throw_pins_from = int((input()))
    throw_pins_to = int((input()))
    #pins_list = ["." for elem in range(throw_pins_from, throw_pins_to)]
    for elem in range(throw_pins_from - 1, throw_pins_to):
        pins_list[elem] = "."
print(pins_list)
