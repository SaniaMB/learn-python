# Conditional expressions = provide a one-line shortcut for if-else statements (ternary operators)
#Print one of two values based on condition
# Syntax: X if condition else Y

num = 5
a = 6
b = 7
age = 13
temperature = 20
user_role = "guest"

result = "Positive" if num > 0 else "Negative"
print("Number is:", result)

parity = "EVEN" if num % 2 == 0 else "ODD"
print("Number is:", parity)

max_num = a if a > b else b
print("Maximum number is:", max_num)

min_num = a if a < b else b
print("Minimum number is:", min_num)

status = "Adult" if age >= 18 else "Child"
print("Person is:", status)

weather = "HOT" if temperature > 20 else "COLD"
print("Weather is:", weather)

access_level = "Full Access" if user_role == "admin" else "Limited Access"
print("Access level:", access_level)