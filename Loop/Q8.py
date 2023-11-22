number = int(input("Enter a number: "))
factor_sum = 0

for i in range(1, number + 1):
    if (number % i == 0):
        factor_sum += i
print("The sum of factors is: ", factor_sum)
