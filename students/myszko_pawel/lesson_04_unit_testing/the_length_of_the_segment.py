
def distance(a, b, c, d): 
    distance = ((c-a)**2 + (d-b)**2)**(.5) 
    return distance

def main():
    x_1 = float(input())
    y_1 = float(input())
    x_2 = float(input())
    y_2 = float(input())

    print(distance(x_1, y_1, x_2, y_2))

if __name__ == '__main__':
    main()
