import math
# Arithmatic Operators
# Compound Operators

friends = 10
#friends += 5
#friends -= 5;
#friends *= 5;
#friends /= 5;    #(float division)
#friends //= 5    #(floor division)
#friends += 5;
#friends **= 2
print(friends)
print()
#  Python’s math module
x = 3.14
y = -4
z = 5

"""
print(round(x))
print(abs(y))
print(pow(4,3))
print(max(x,y,z))
print(min(x,y,z))
print()

print(math.pi)
print(math.e)
print(math.sqrt(25))
print(math.ceil(x))
print(math.floor(x))
"""

# circumference of a circle (2*pi*r)

radius = float(input("Enter the radius of the circle: "))
cir = 2 * math.pi * radius
print(f"The circumference is: {round(cir,2)} cm")
print()

# Area of a circle (pi*r**2)

radius = float(input("Enter the radius of the circle: "))
area = math.pi * radius ** 2
#area = math.pi * pow(radius, 2)
print(f"The area of ths circle is: {round(area,2)} cm")
print()

# Calculating the hypotenuse

a = float(input("Enter side A: "))
b = float(input("Enter side B: "))
c = math.sqrt(pow(a,2)+pow(b,2))
print(f"The side is equal to {round(c,2)}")