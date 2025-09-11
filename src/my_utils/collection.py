# Collection = single "variable" used to store multiple values
# List       = [] ordered and changeable. Duplicates OK
# Set        = {} unordered and immutable, but Add/Remove is OK. No duplicates
# Tuple      = () ordered and unchangeable, Duplicate is OK. FASTER

#List
fruits = ["apple","orange","banana",1,5]

print(fruits[3])
print(fruits[0:3])
print(fruits)
print(fruits[::2])
print(fruits[::-1])
print(len(fruits))
print("apple" in fruits)
fruits[3] = "pineapple"
fruits.append("strawberry")
fruits.remove("apple")
fruits.insert(0,"dragon fruit")
#print(fruits.reverse())
# fruits.clear()
print(fruits.index("pineapple"))
print(fruits.count("banana"))
print()
for fruit in fruits:
    print(fruit)

print()
print("SET")
#Set
# No indexing on set
fruits1 ={"apple","orange","banana","pineapple","coconut","coconut"}
fruits1.add("mango")
fruits1.pop()
#fruits1.clear()
print(fruits1)
print()

#Tuple
print("Tuple")
fruits2 =("apple","orange","banana","pineapple","coconut","coconut")
print(len(fruits2))
print("apple" in fruits2)
print(fruits2.index("apple"))
print(fruits2.count("coconut"))