n = int(input("Enter the number of Fibonacci series numbers: "))
n1 = 0
n2 = 1
count = 1
print("Fibonacci series:")
print(n1)
while count < n:
    print(n2)
    temp = n1 + n2
    n1 = n2
    n2 = temp
    count += 1
