a = int( input() )
b = int( input() ) 
n = int( input() ) 

d = a * n + ( b * n ) // 100
c = ( b * n ) % 100

print( str(d) + " " + str(c) )
