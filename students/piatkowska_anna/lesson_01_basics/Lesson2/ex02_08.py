#Statement
#A cupcake costs A dollars and B cents. 
#Determine, how many dollars and cents should one pay for N cupcakes. 
#A program gets three numbers: A, B, N. It should print two numbers: total cost in dollars and cents.
print("Please enter cupcake cost:")
print("Enter dollars value:")
a = int(input())
print("Enter cents value:")
b = int(input())
print("Enter quantity of cupcakes:")
c = int(input())
print("Total cost is: " + str(a*c+b*c//100) + " dollars, " +str(b*c%100) + " cents")