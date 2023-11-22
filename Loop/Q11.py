start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

print("Squares of natural numbers between ", start, " and ", end, ":")
for i in range(start, end + 1):
    square = i ** 2
    print("The square of ", i, " is: ", square)
