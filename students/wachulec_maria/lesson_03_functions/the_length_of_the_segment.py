def distance(x1, y1, x2, y2):
    d = ((x2 - x1)**2 + (y2 - y1)**2)**(1/2)
    print(d)


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
distance(x1, y1, x2, y2)