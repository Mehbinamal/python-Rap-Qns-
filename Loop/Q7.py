n = int(input("Enter a number: "))
num = n ** 2
k = 0
n1 = n
while (n1 > 0):
    n1 = n1 // 10
    k = k + 1
digits = num % (10 ** k)
if (digits == n):
    print("Number is automorphic")
else:
    print("Number is not automorphic")
