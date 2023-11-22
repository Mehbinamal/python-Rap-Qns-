n = int(input("Enter the number of terms needed :"))
s = 0
for i in range(1, n+1):
    s += ((i**2)*((-1)**(i-1)))
print("Sum of the series of ", n, " terms = ", s)
