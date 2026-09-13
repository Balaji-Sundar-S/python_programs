"""This program takes an integer as input from the user and finds the largest digit in it. It then prints the result to the console."""

num = int(input("Enter a number: "))
largest_digit = 0
temp = num
while temp > 0:
    digit = temp % 10
    if digit > largest_digit:
        largest_digit = digit
    temp //= 10
print("The largest digit in", num, "is:", largest_digit)