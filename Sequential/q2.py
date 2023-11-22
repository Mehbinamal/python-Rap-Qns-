s1 = int(input("Enter side1 :"))
s2 = int(input("Enter side2 :"))
s3 = int(input("Enter side3 :"))
p = s1+s2+s3
s = p/2
area = (s*(s-s1)*(s-s2)*(s-s3)) ** (1/2)
print("Perimeter = ", p)
print("Area = ", area)
