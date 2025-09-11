# Dictionary = a collection of {key:value} pairs
#              ordered and changeable. No duplicates

capitals = {"USA": "Washington D.C",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}

#print(dir(capitals))
#print(help(capitals))
print(capitals.get("Japan"))

if capitals.get("Russia"):
    print("That capital exists")
else:
    print("The capital doesn't exist")

capitals.update({"Germany": "Berlin"})
capitals.update({"USA": "Detroit"})
capitals.pop("China")
capitals.popitem() # removes the lastest key value pair

keys = capitals.keys()
print(keys)
print()

for key in capitals.keys():
    print(key)
print()

for value in capitals.values():
    print(value)
print()

items = capitals.items()
print(items)
print()

for key,value in capitals.items():
    print(f"{key}: {value}")
