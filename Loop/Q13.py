x = int(input("Enter a Number :"))
n = int(input("Enter the power of the number :"))
i = 0
p=1
while(i != n):
    p *= x
    i += 1
print("Answer = ", p)
