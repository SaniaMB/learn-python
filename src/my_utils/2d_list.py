# Two-dimensional list

fruits =    ["aplle","orange","banana","coconut"]
vegetable = ["celery","carrots","potatoes"]
meats =     ["chicken","fish","turkey"]

groceries = [fruits,vegetable,meats]

print(groceries[0])
print(groceries[1])
print(groceries[2])

print(groceries[0][1])
print(groceries[1][2])

for collection in groceries:
    for food in collection:
        print(food, end =' ')
    print()

#Numpad
print()
num_pad = ((1,2,3),
           (4,5,6),
           (7,8,9),
           ("*",0,"#"))

for row in num_pad:
    for num in row:
        print(num,end = " ")
    print()