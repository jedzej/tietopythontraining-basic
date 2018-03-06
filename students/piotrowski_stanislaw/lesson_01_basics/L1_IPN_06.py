#https://snakify.org/lessons/print_input_numbers/problems/school_desks/
#piotrsta

print('Liczba uczniow w klasie A: ')
studA = int(input())
print('Liczba uczniow w klasie B: ')
studB = int(input())
print('Liczba uczniow w klasie C: ')
studC = int(input())

deskA=int((studA/2)+(studA%2))
deskB=int((studB/2)+(studB%2))
deskC=int((studC/2)+(studC%2))
#print(deskA)
#print(deskB)
#print(deskC)
deskABC=deskA+deskB+deskC
print('Potrzeba '+str(deskABC)+' biurek, dla uczniow z klas A, B i C.')


