# logical operators = Evaluate multiple conditions (and, or, not),
#                or = at least one condition must be true,
#               and = both conditions must be true
#               not = inverts the condition (not false, not true)

temp = 0
is_raining = False

if temp > 35 or temp < 0 or is_raining:
    print("The outdoor event is canceled")
else:
    print("The outdoor event is till scheduled")
print()

is_sunny = False

if temp >= 28 and is_sunny:
    print("It is HOT outside 😡")
    print("It is SUNNY 🌞")
elif temp <= 0 and is_sunny:
    print("It is COLD outside 🥶")
    print("It is SUNNY 🌞")
elif 28 > temp > 0 and is_sunny:
    print("It is WARM outside 🙂")
    print("It is SUNNY 🌞")
elif temp >= 28 and not is_sunny:
    print("It is HOT outside 😡")
    print("It is CLOUDY ☁️")
elif temp <= 0 and not is_sunny:
    print("It is COLD outside 🥶")
    print("It is CLOUDY ☁️")
elif 28 > temp > 0 and not is_sunny:
    print("It is WARM outside 🙂")
    print("It is CLOUDY ☁️")
