"""This program takes an integer as input from the user and counts the number of digits in it. It then prints the result to the console."""

num = int(input("Enter an integer: "))
temp = num
c = 0
while temp > 0:
    c += 1
    temp = temp // 10
if num == 0:
    c = 1
print("The number of digits in", num, "is:", c)