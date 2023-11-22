a = int(input("Enter coefficient of 'X^2' :"))
b = int(input("Enter coefficient of 'X':"))
c = int(input("Enter constant term : "))
d = ((b**2)-4*a*c)
if (d==0):
    print("Equation has Equal Real Roots")
elif (d>0):
    print("Equation has 2 real roots")
else :
    print("Equation has imaginary Roots")
