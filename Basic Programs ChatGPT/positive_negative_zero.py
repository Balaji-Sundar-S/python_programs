"""This program takes an integer as input from the user and checks whether it is positive, negative, or zero. It then prints the result to the console."""

num = int(input("Enter an integer: "))
if num > 0:
    print(num, "is a positive number.")
elif num < 0:
    print(num, "is a negative number.")
else:
    print(num, "is zero.")