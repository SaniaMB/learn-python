# Python weight converter program

weight = float(input("Enter your weight: "))
unit = input("Kilograms or Pounds? (K / L): ")

if unit == 'K':
    weight *= 2.205
    unit = 'Lbs'
elif unit == 'L':
    weight /= 2.205
    unit = 'kg'
else:
    print(f"unit {unit} was not valid!")

print(f"Your weight is {round(weight,2)} {unit}")
