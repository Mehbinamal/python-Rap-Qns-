binary = int(input("Enter a Binary number :"))
num = 0
i = 0
while(binary>0):
    digit = binary % 10
    num = num + (digit*(2**i))
    i = i+1
    binary = binary//10
print("Number = ", num)
