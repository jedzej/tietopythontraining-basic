#Statement
#N students take K apples and distribute them among each other evenly. 
#The remaining (the undivisible) part remains in the basket. 
#How many apples will each single student get? 
#How many apples will remain in the basket?
#The program reads the numbers N and K. It should print the two answers for the questions above. 
print("Enter students number")
a = int(input())
print("Enter number of apples:")
b = int(input())
print("Each student gets " + str(b//a) +" apples")
print("In the basket remains " + str(b%a) + " apples")