def Roots(a, b, c):
    d = b**2 - 4*a*c
    if (d < 0):
        real = -b/(2*a)
        imag = -d**0.5/(2*a)
        print("x1:", real, "+", imag)
        print("x2:", real, "-", imag)
        
    elif (d == 0):
        real = -b/(2*a)
        print("x1:", real)
        print("x2:", real)
        
    elif (d > 0):
        x1 = (-b + d**0.5)/(2*a)
        x2 = (-b - d**0.5)/(2*a)
        print("x1:", x1)
        print("x2:", x2)
        
    print("General Solution: C1(", x1, ")^n + C2(", x2, ")^n")
    
if __name__ == "__main__":
    a = float(input("a: "))
    b = float(input("b: "))
    c = float(input("c: "))
    Roots(a, b, c)
