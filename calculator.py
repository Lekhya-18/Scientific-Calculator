import math
import sys
def add(x,y):
    return x+y
def sub(a,b):
    return a-b
def mul(m,n):
    return m*n
def div(l,s):
    if s==0:
        return "ZeroDivisionError- output is Infinite"
    else:
        return l/s
def mod(x,y):
    if y==0:
        return "ZeroDivisionError - output is infinite"
    else:
        return x%y
def reciprocal(z):
    if z==0:
        return "ZeroDivisionError - output is infinite"
    else:
        return 1/z
def power(b,p):
    return b**p
def sqrt(n):
    if n < 0:
        return "ValueError - input must be a non-negative number"
    else:
        return math.sqrt(n)
def exponent(b,p):
    return math.exp(b*p)
def logarithm(c,d):
    if c<=0 or d<=0:
        return "ValueError - log base and value must be greater than 0"
    else:
        return math.log(c,d)
def trigonometry(angle, func):
    angle_rad = math.radians(angle)
    if func == "sin":
        return math.sin(angle_rad)
    elif func == "cos":
        return math.cos(angle_rad)
    elif func == "tan":
        return math.tan(angle_rad)
    else:
        return "Invalid trigonometric function"
def factorial(n):
    if n<0:
        return "ValueError - input must be a non-negative integer"
    elif n==0:
        return 1
    else:
        return n * factorial(n-1)
def quadratic_equation(a,b,c):
    if a==0:
        return "ValueError - 'a' must be non-zero"
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return "ValueError - no real roots"
    root1 = (-b + math.sqrt(discriminant)) / (2*a)
    root2 = (-b - math.sqrt(discriminant)) / (2*a)
    return (root1, root2)
def unknown_from_quation(no_of_unknowns):
    if no_of_unknowns == 1:
        print("Single variable equation, please provide the equation in the form ax + b = 0")
        print("Enter the cofficients a and b:")
        a,b= map(float, input().split())
        x = (-b)/a
        return x  
    elif no_of_unknowns == 2:
        print("Two variable equation, please provide the equations in the form a1x + b1y + c1 =0 and a2x +b2y + c2 = 0")
        print("Enter the cofficients a1, b1, c1, a2, b2, c2:")
        a1,b1,c1,a2,b2,c2 = map(float, input().split())
        d = a1 * b2 - a2 * b1
        if d==0:
            return "ValueError - no unique solution exists"
        y = (a2*c1 - a1*c2) / d
        x = (c1 - b1*y) / a1
        return (x, y)
    elif no_of_unknowns == 3:
        print("Three variable equation, please provide the equations in the form a1x + b1y + c1z = 0, a2x + b2y + c2z = 0, a3x + b3y + c3z = 0")
        print("Enter the coefficients a1, b1, c1, a2, b2, c2, a3, b3, c3:")
        a1, b1, c1, a2, b2, c2, a3, b3, c3 = map(float, input().split())
        # Solve using elimination or substitution
        d1 = a1 * b2 - a2 * b1
        d2 = a1 * b3 - a3 * b1
        if d1 == 0 or d2 == 0:
            return "ValueError - no unique solution exists"
        y = (a2*c1 - a1*c2) / d1
        z = (a3*c1 - a1*c3) / d2
        x = (c1 - b1*y - c1*z) / a1
        return (x, y, z)
    else:
        return "This calculator currently supports up to three unknowns only"
def quit():
    print("Thank you for using the calculator!")
    sys.exit(0)

def available_operations():
    print("Welcome to the calculator!")
    print("Available operations:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Reciprocal")
    print("7. Power")
    print("8. Square Root")
    print("9. Exponentiation")
    print("10. Logarithm")
    print("11. Trigonometry (sin, cos, tan)")
    print("12. Factorial")
    print("13. Quadratic Equation Solver")
    print("14. Unknown Variable Solver (up to 3 variables)")
    print("15. Quit calculator")
    print("___________________________")

def main():
    available_operations()
    print("\nSelect an operation")
    while True:
        choice = input("Enter the number of the operation you want to perform (or '15' to quit): ")
        if choice == "1":
            x, y = map(float, input("Enter two numbers (x y): ").split())
            print("Result:", add(x, y))
        elif choice == "2":
            a, b = map(float, input("Enter two numbers (a b): ").split())
            print("Result:", sub(a, b))
        elif choice == "3":
            m, n = map(float, input("Enter two numbers (m n): ").split())
            print("Result:", mul(m, n))
        elif choice == "4":
            l, s = map(float, input("Enter two numbers (l s): ").split())
            print("Result:", div(l, s))
        elif choice == "5":
            x, y = map(float, input("Enter two numbers (x y): ").split())
            print("Result:", mod(x, y))
        elif choice == "6":
            z = float(input("Enter a number (z): "))
            print("Result:", reciprocal(z))
        elif choice == "7":
            b, p = map(float, input("Enter base and power (b p): ").split())
            print("Result:", power(b, p))
        elif choice == "8":
            n = float(input("Enter a non-negative number (n): "))
            print("Result:", sqrt(n))
        elif choice == "9":
            b, p = map(float, input("Enter base and power (b p): ").split())
            print("Result:", exponent(b, p))
        elif choice == "10":
            c, d = map(float, input("Enter base and value (c d): ").split())
            print("Result:", logarithm(c, d))
        elif choice == "11":
            angle = float(input("Enter angle in degrees: "))
            func = input("Enter trigonometric function (sin, cos, tan): ")
            print("Result:", trigonometry(angle, func))
        elif choice == "12":
            n = int(input("Enter a non-negative integer (n): "))
            print("Result:", factorial(n))
        elif choice == "13":
            a, b, c = map(float, input("Enter coefficients a, b, c: ").split())
            print("Result:", quadratic_equation(a, b, c))
        elif choice == "14":
            no_of_unknowns = int(input("Enter the number of unknowns (1-3): "))
            print(unknown_from_quation(no_of_unknowns))
        elif choice == "15":
            quit()
        elif choice in [str(i) for i in range(1, 14)]:
            break
        else:
            print("Invalid choice, please try again.")
            
if __name__ == "__main__":
    main()