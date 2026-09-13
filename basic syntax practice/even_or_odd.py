"""This program takes an integer as input from the user and checks whether it is even or odd. It then prints the result to the console."""

num = int(input("Enter an integer: "))
if num % 2 == 0:
    print(num, "is an even number.")
else:
    print(num, "is an odd number.")