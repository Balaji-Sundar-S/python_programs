"""This program takes a starting and ending number as input from the user and calculates the sum of all numbers in that range (inclusive). It then prints the result to the console."""

start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))
sum_of_numbers = 0
for i in range(start, end + 1):
    sum_of_numbers += i
print("The sum of numbers from", start, "to", end, "is:", sum_of_numbers)