# Program return distance between point A and B.
import math
    
def distance(x1, y1, x2, y2):
    vector = math.fabs(math.sqrt((x2 - x1) ** 2 + (y2 - y1)**2))
    vector = round(vector, 5)
    print ("Lenght of vector is:", vector)
    return vector

try:
  x1 = int((input("x1:")))
  y1 = int((input("y1:")))
  x2 = int((input("x2:")))
  y2 = int((input("y2:")))
  
  distance(x1, y1, x2, y2)
  
except ValueError:
   print("It isn't integer!")
