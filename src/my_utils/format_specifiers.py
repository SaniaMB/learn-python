# format specifiers = {value:flags} format a value based on what flags are inserted
#
# .(number)f  = round to that many decimal places (fixed point)
# (number)    = allocate that many spaces
# 0(number)   = allocate and zero pad that many spaces
# <           = left justify
# >           = right justify
# ^           = center align
# +           = use a plus sign to indicate positive value
# =           = place sign to leftmost position
# (space)     = insert a space before positive numbers
# ,           = comma separator

price1 = 3000.14159
price2 = -9870.65
price3 = 12000.34

print(f"Price 1 is ${price1:.2f}")      # .(number)f = round to that many decimal places (fixed point)
print(f"Price 2 is ${price2:10}")       #  (number) = allocate that many spaces
print(f"Price 3 is ${price3:010}")      # 0(number) = allocate and zero pad that many spaces
print()

print(f"Price 1 is ${price1:<10}")      # < = left justify
print(f"Price 2 is ${price2:>10}")      # > = right justify
print(f"Price 3 is ${price3:^10}")      # ^ = center align
print()

print(f"Price 1 is ${price1:+}")        # + = use a plus sign to indicate positive value
print(f"Price 2 is ${price2:+}")
print(f"Price 3 is ${price3:+}")
print()

print(f"Price 1 is ${price1: }")        # (space) = insert a space before positive numbers
print(f"Price 2 is ${price2: }")
print(f"Price 3 is ${price3: }")
print()

print(f"Price 1 is ${price1:=}")        # = = place sign to leftmost position
print(f"Price 2 is ${price2:=}")
print(f"Price 3 is ${price3:=}")
print()

print(f"Price 1 is ${price1:,}")        # , = comma separator
print(f"Price 2 is ${price2:,}")
print(f"Price 3 is ${price3:,}")
print()

print(f"Price 1 is ${price1:+,.2f}")