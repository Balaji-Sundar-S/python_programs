"""This program takes an integer as input from the user and prints its multiplication table from 1 to 10. It then prints the result to the console."""

num = int(input("Enter an integer: "))
for i in range(1, 11):
    product = num * i
    print(num, "x", i, "=", product)