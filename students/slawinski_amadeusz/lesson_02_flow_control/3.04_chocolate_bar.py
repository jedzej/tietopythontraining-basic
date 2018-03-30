# can we get target amount of squares when dividing width x height chocolate

width = int(input())
height = int(input())
squares = int(input())

# check if there is enough squares and then check if we can divide in any
# dimension without leftovers
if width * height >= squares and (squares % width == 0 or
   squares % height == 0):
    print("YES")
else:
    print("NO")
