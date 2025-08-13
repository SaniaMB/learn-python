text = "  Hello, Python World!  "

# 1. strip() - Remove leading/trailing spaces
print(text.strip())  # "Hello, Python World!"

# 2. lower() - Convert to lowercase
print(text.lower())  # "  hello, python world!  "

# 3. upper() - Convert to uppercase
print(text.upper())  # "  HELLO, PYTHON WORLD!  "

# 4. title() - Capitalize each word
print(text.title())  # "  Hello, Python World!  "

# 5. replace() - Replace parts of the string
print(text.replace("Python", "Java"))  # "  Hello, Java World!  "

# 6. split() - Split string into list
print(text.split())  # ['Hello,', 'Python', 'World!']

# 7. join() - Join list into string
words = ["I", "love", "Python"]
print(" ".join(words))  # "I love Python"

# 8. find() - Find first occurrence (returns index or -1)
print(text.find("Python"))  # 9

# 9. count() - Count occurrences
print(text.count("o"))  # 3

# 10. startswith() / endswith()
print(text.strip().startswith("Hello"))  # True
print(text.strip().endswith("World!"))   # True

text = "I have 2 apples and 10 bananas"

# find() - returns the index of the first occurrence
print(text.find("apple"))   # 7

# rfind() - returns the index of the last occurrence
print(text.rfind("a"))      # 26

# isalpha() - True if all characters are letters (no spaces, digits, symbols)
word1 = "Hello"
word2 = "Hello123"
print(word1.isalpha())  # True
print(word2.isalpha())  # False

# isdigit() - True if all characters are digits
num1 = "12345"
num2 = "12a45"
print(num1.isdigit())   # True
print(num2.isdigit())   # False