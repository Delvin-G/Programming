## Name: Pyan McMaster
# Date: 2026-11-12
#program: Carpet Cost Example
# desc: Calculate cost to carpet room

# Named constant for the install fee
INSTALL_FEE = 25.00

# Input: room owner, cost per square foot, a
owner = input("Owner:")
cost_per_foot  = float(input("cost per square foot"))
square_feet = int(input("Square feet: "))

# Processing: Material vost and total
material_cost = cost_per_foot * square_feet
tital_cost = material_cost + INSTALL_FEE

#OUTPUT: a small report, format $ to 2 decimals
print()
print()
print()
print()
