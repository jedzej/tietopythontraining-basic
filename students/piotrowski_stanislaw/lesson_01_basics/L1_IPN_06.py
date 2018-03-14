#https://snakify.org/lessons/print_input_numbers/problems/school_desks/
#piotrsta
import math

studA = int(input('Liczba uczniow w klasie A: '))
studB = int(input('Liczba uczniow w klasie B: '))
studC = int(input('Liczba uczniow w klasie C: '))

deskA = math.ceil(studA/2)
deskB = math.ceil(studB/2)
deskC = math.ceil(studC/2)

deskABC = deskA + deskB + deskC
print('Potrzeba ' + str(deskABC) + ' biurek, dla uczniow z klas A, B i C.')
