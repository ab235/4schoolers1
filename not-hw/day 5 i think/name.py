import sys

def main():
    args = list(map(int,sys.argv[3:]))
    area = 0
    perimeter = 0
    if (sys.argv[2] == "triangle"):
        s = sum(args)/2
        a = args[0]
        b = args[1]
        c = args[2]
        area = ((s)*(s-a)*(s-b)*(s-c))**0.5
        perimeter = a + b + c
    elif (sys.argv[2] == "circle"):
        r = args[0]
        area = 3.14159 * r * r
        perimeter = 3.14159 * 2 * r
    else:
        a = args[0]
        b = args[1]
        area = a*b
        perimeter = 2*a + 2*b
    if (sys.argv[1] == "area"):
        print("Area: " + str(area))
    else:
        print("Perimeter: " + str(perimeter))

if (__name__ == "__main__"):
    main()
