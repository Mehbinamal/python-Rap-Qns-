n = int(input("Enter a number : "))
if (n>9 and n<100 ) :
    a = n % 10
    b = n // 10
    if (a>=b):
        print(b, " Is the smallest number")
    else :
        print(a, " Is the smallest number")
else:
    print("It is not a double digit number, please Enter a double digit number")
