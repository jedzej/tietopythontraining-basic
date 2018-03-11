a = int(input("Enter dollars: "))
b = int(input("Enter cents: "))
n = int(input("Enter amount of cupcakes: "))
print (str(((((a*100) + b) * n)) // 100) + " " +  str(((((a * 100) + b) * n)) % 100))
