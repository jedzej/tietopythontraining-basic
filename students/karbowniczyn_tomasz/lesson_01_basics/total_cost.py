#total cost
#by tk

dols = int(input()) 
cents = int(input()) 
cakes = int(input()) 

price = ((100*dols+cents)*cakes)
#print (price)

ileDol =  (str(price//100))
ileCent =  (str(price % 100))

print (ileDol)
print (ileCent)



