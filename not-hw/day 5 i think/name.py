import sys

def main():
    args = sys.argv
    area = 0
    perimeter = 0
    if (args[2] == "triangle"):
        s = sum(args[3:])
        a = args[3]
        b = args[4]
        c = args[5]
        area = ((s)*(s-a)*(s-b)*(s-c))**0.5
        perimeter = a + b + c
    elif (args[2] == "circle"):
        r = args[3]
        area = 3.14159 * r * r
        perimeter = 3.14159 * 2 * r
    else:
        a = args[3]
        b = args[4]
        area = a*b
        perimeter = 2*a + 2*b
    if (args[1] == "area"):
        print("Area: " + str(area))
    else:
        print("Perimeter: " + str(perimeter))

if (__name__ == "__main__"):
    main()
