h = int( input() )
m = int( input() )
s = int( input() )

hd = 360 /12 
md = 360 / 720
sd = 360 / 43200

d = h * hd + m * md + s * sd
print( d )
