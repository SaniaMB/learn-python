"""
 Type Casting - Type casting means converting a variable from one data type to another.
 In Python, this is usually done using constructor functions like int(), float(), str(), etc.
"""

# Integer to float
x = 10
y = float(x)
print(y)        # 10.0
print(type(y))  # <class 'float'>

# String to int
num_str = "25"
num_int = int(num_str)
print(num_int + 5)  # 30

# Float to int (decimal part is dropped)
pi = 3.1416
pi_int = int(pi)
print(pi_int)   # 3
