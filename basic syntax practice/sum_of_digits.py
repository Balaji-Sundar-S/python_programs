"""This program takes an integer as input from the user and calculates the sum of its digits. It then prints the result to the console."""

num = int(input("Enter a number: "))
sum_of_digits = 0
temp = num
while temp > 0:
    digit = temp % 10
    sum_of_digits += digit
    temp //= 10
print("The sum of digits in", num, "is:", sum_of_digits)