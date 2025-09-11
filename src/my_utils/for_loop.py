# For loops = execute a block of code a fixed number of times.
#             You can iterate over a range, string, sequence, etc.

for x in reversed(range(1,11)):
    print(x)
print("HAPPY NEW YEAR!")
print()

for x in range(1,11,2):
    print(x)
print()

credit_card = "1234-5678-9012-3456"
for x in credit_card:
    print(x,end = "")  # You can just do print(credit_card) but we wanna be extra
print()
print()

for x in range(1,21):
    if x == 13:
      continue         # can try break here too
    else:
        print(x,end = " ")