n = int(input("Enter a number :"))
s = 0
n1 = n
n2 = n
k = 0
while (n1 > 0):
    n1 = n1 // 10
    k = k + 1
while(n2>0):
    digit = n2 % 10
    s += (digit**k)
    n2 = n2//10
if (n==s):
    print("Number is Armstrong ")
else:
    print("Number is not Armstrong")
