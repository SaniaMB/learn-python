# Validate User input
# 1 Username cannot be no more than 12 characters
# 2 Username must not contain spaces
# 3 Username must not contain numbers

username = input("Enter your Username: ")

if len(username) > 12:
    print("Your Username can't be more than 12 characters")
elif not username.find(' ') == -1:
    print("Your Username cannot contain spaces")
elif not username.isalpha():
    print("Your Username cannot contain numbers")
else:
    print(f"Welcome {username}")
