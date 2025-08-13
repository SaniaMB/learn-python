#  Basic User Input
name = input("Enter your name: ")
print("Hello,", name)

#  Converting Input to Other Types
age = int(input("Enter your age: "))   # converts to int
height = float(input("Enter your height in feet: "))  # converts to float

print("Age:", age)
print("Height:", height)

# Taking Multiple Inputs
x, y = map(int, input("Enter two numbers separated by space:: ").split())
print("Sum =", x + y)

"""
.split() → ["10", "20"]
map(int, ...) → applies int() to each element
Now x = 10 (int), y = 20 (int)
Addition works: x + y = 30
"""

# Comma-separated values
numbers = input("Enter numbers separated by commas: ").split(",")
print(numbers)  # list of strings

#  Example Program
name = input("Enter your name: ")
age = int(input("Enter your age: "))
score1, score2 = map(float, input("Enter two scores: ").split())

print(f"Hello {name}, you are {age} years old.")
print("Total score:", score1 + score2)
