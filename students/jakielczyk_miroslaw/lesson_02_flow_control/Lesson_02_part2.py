# Factorial
n = int(input())
silnia = 1
for x in range (1, n+1) :
    silnia *= x
print (silnia)


# The number of zeros
n = int(input())
zeros_number = 0
for x in range (n) :
    if int(input()) == 0 :
        zeros_number += 1
print (zeros_number)


# Adding factorials
n = int(input())
summary = 0
silnia = 1
for x in range (1, n+1) :
    silnia *= x
    summary += silnia
print (summary)


# Ladder
n = int(input())
for x in range (1, n+1):
    for y in range (1, x+1):
        print (y, sep='', end='')
    print ('')


# Lost card
n = int(input())
cards_list = []
for x in range (n-1):
    cards_list.append(int(input()))
for x in range (1, n+1) :
    card_found = False
    for card in cards_list :
        if x == card :
            card_found = True
    if not card_found :
        print (x)
        break
    
