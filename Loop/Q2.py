n = int(input("Enter a number :"))
n1=n
s = 0
while (n1>0):
    a = n1 % 10
    s = a + (s*10)
    n1 = n1//10
if (s==n):
    print("Number is palindrome")
else:
    print("Number is not palindrome")
