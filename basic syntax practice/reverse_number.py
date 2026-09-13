"""This program takes an integer as input from the user and reverses its digits. It then prints the reversed number to the console."""

num = int(input("Enter an integer: "))
rev = 0
temp = num
while temp > 0:
    rem = temp % 10
    temp = temp // 10
    rev = rev * 10 + rem
print("The reverse of", num, "is:", rev)