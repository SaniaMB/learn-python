# if -> Do some code only IF some condition is true
# else -> do something else

age = int(input("Enter your age: "))
if age >= 18:
    print("Your are now signed up!")
elif age < 0:
    print("You haven't even been born yet")
else:
    print("You need to be 18+ to sign up")
print()
#

response = input("Would You like food(Y/N): ").lower()
if response == 'y':
    print("Ok have some food!")
else:
    print("No food for you")
print()
 #

name = input("Enter Your name:")
if name == '':
    print("You did not enter your name!")
else :
    print(f"Hi {name}")
