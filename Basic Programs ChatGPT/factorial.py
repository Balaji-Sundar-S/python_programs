"""This program takes an integer as input from the user and calculates its factorial. It then prints the result to the console."""

num = int(input("Enter an integer: "))
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print("The factorial of", num, "is:", factorial)