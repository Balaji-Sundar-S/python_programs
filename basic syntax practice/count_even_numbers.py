"""This program takes a starting and ending number as input from the user and counts the number of even numbers in that range (inclusive). It then prints the result to the console."""

start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))
count = 0
for i in range(start, end + 1):
    if i % 2 == 0:
        count += 1
print("The number of even numbers from", start, "to", end, "is:", count)