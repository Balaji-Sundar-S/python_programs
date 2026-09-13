"""This program takes two integers as input from the user and compares them to determine which one is larger. It then prints the result to the console."""

first_integer = int(input("Enter the first integer: "))
second_integer = int(input("Enter the second integer: "))
if first_integer > second_integer:
    print(first_integer, "is larger than", second_integer)
elif second_integer > first_integer:
    print(second_integer, "is larger than", first_integer)
else:
    print("Both integers are equal.")